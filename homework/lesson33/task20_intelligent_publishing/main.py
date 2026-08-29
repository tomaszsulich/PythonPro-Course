import json
import re
from collections.abc import AsyncGenerator, Awaitable, Callable
from contextlib import asynccontextmanager

from fastapi import (
    BackgroundTasks,
    Depends,
    FastAPI,
    Header,
    HTTPException,
    Request,
    Response,
    status,
)
from fastapi.responses import JSONResponse
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from ai_service import (
    summarize_post,
    violates_ai_moderation,
    violates_content_policy,
)
from database import Base, engine, get_db
from models import Comment, Post, User
from schemas import (
    CommentCreate,
    CommentResponse,
    CommentUpdate,
    PostCreate,
    PostResponse,
    PostSummaryResponse,
    PostUpdate,
    PostWithCommentsResponse,
    UserCreate,
    UserCreateResponse,
    UserResponse,
    UserUpdate,
)
from tasks import analyze_comment_sentiment, send_comment_email


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None]:
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)

    yield

    await engine.dispose()


app = FastAPI(lifespan=lifespan)


PROFANITY_PATTERNS = (
    r"\bkurw\w*",
    r"\bpierdol\w*",
    r"\bjeb\w*",
    r"\bchuj\w*",
    r"\bk[\W_]*u[\W_]*r[\W_]*w[\W_]*\w*",
    r"\bp[\W_]*i[\W_]*e[\W_]*r[\W_]*d[\W_]*o[\W_]*l\w*",
    r"\bj[\W_]*e[\W_]*b\w*",
    r"\bc[\W_]*h[\W_]*u[\W_]*j\w*",
)


def contains_profanity(content: str) -> bool:
    normalized = content.casefold()

    return any(
        re.search(pattern, normalized)
        for pattern in PROFANITY_PATTERNS
    )


async def should_moderate_request(request: Request) -> bool:
    if request.method not in {"POST", "PUT", "PATCH"}:
        return False

    path = request.url.path

    if path == "/users":
        return True

    if re.fullmatch(r"/users/\d+", path):
        return True

    if path == "/posts":
        return True

    if re.fullmatch(r"/posts/\d+", path):
        return True

    if re.fullmatch(r"/posts/\d+/comments", path):
        return True

    if re.fullmatch(r"/comments/\d+", path):
        return True

    return False


@app.middleware("http")
async def moderate_content(request: Request,
                           call_next: Callable[[Request], Awaitable[Response]]) -> Response:
    if not await should_moderate_request(request):
        return await call_next(request)

    body = await request.body()

    if not body:
        return await call_next(request)

    try:
        data = json.loads(body)
    except json.JSONDecodeError:
        return await call_next(request)

    for field in ("name", "title", "content"):
        value = data.get(field)

        if not isinstance(value, str):
            continue

        if field != "name" and contains_profanity(value):
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={"detail": "Treść zawiera niedozwolone wulgaryzmy."},
            )

        if field != "name" and await violates_ai_moderation(value):
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={"detail": "Treść narusza zasady moderacji."},
            )

        if await violates_content_policy(value, field):
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={"detail": "Treść narusza zasady publikacji."},
            )

    return await call_next(request)


async def get_current_user(x_api_key: str = Header(alias="X-API-Key"),
                           db: AsyncSession = Depends(get_db)) -> User:
    result = await db.execute(
        select(User).where(User.api_key == x_api_key)
    )
    user = result.scalar_one_or_none()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Nieprawidłowy klucz API."
        )

    return user


@app.post("/users", response_model=UserCreateResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user_data: UserCreate,
                      db: AsyncSession = Depends(get_db)) -> User:
    result = await db.execute(
        select(User).where(User.email == str(user_data.email))
    )

    if result.scalar_one_or_none() is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Użytkownik z tym adresem e-mail już istnieje."
        )

    user = User(**user_data.model_dump())

    db.add(user)
    await db.commit()
    await db.refresh(user)

    return user


@app.get("/users", response_model=list[UserResponse])
async def get_users(db: AsyncSession = Depends(get_db)) -> list[User]:
    result = await db.execute(select(User))
    return list(result.scalars().all())


@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int,
                   db: AsyncSession = Depends(get_db)) -> User:
    user = await db.get(User, user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nie znaleziono użytkownika."
        )

    return user


@app.put("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: int,
                      user_data: UserCreate,
                      db: AsyncSession = Depends(get_db)) -> User:
    user = await db.get(User, user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nie znaleziono użytkownika."
        )

    result = await db.execute(
        select(User).where(
            User.email == str(user_data.email),
            User.id != user_id,
        )
    )

    if result.scalar_one_or_none() is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Użytkownik z tym adresem e-mail już istnieje."
        )

    user.name = user_data.name
    user.email = user_data.email

    await db.commit()
    await db.refresh(user)

    return user


@app.patch("/users/{user_id}", response_model=UserResponse)
async def patch_user(user_id: int,
                     user_data: UserUpdate,
                     db: AsyncSession = Depends(get_db)) -> User:
    user = await db.get(User, user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nie znaleziono użytkownika."
        )

    updates = user_data.model_dump(exclude_unset=True)

    if not updates:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Nie podano danych do aktualizacji."
        )

    if "email" in updates:
        result = await db.execute(
            select(User).where(
                User.email == str(updates["email"]),
                User.id != user_id,
            )
        )

        if result.scalar_one_or_none() is not None:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Użytkownik z tym adresem e-mail już istnieje."
            )

    for field, value in updates.items():
        setattr(user, field, value)

    await db.commit()
    await db.refresh(user)

    return user


@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int,
                      db: AsyncSession = Depends(get_db)) -> None:
    user = await db.get(User, user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nie znaleziono użytkownika."
        )

    await db.delete(user)
    await db.commit()


@app.post("/posts", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
async def create_post(post_data: PostCreate,
                      current_user: User = Depends(get_current_user),
                      db: AsyncSession = Depends(get_db)) -> Post:
    post = Post(
        **post_data.model_dump(),
        author_id=current_user.id,
    )

    db.add(post)
    await db.commit()
    await db.refresh(post)

    return post


@app.get("/posts", response_model=list[PostResponse])
async def get_posts(db: AsyncSession = Depends(get_db)) -> list[Post]:
    result = await db.execute(select(Post))
    return list(result.scalars().all())


@app.get("/posts/{post_id}", response_model=PostResponse)
async def get_post(post_id: int,
                   db: AsyncSession = Depends(get_db)) -> Post:
    post = await db.get(Post, post_id)

    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nie znaleziono posta."
        )

    return post


@app.put("/posts/{post_id}", response_model=PostResponse)
async def update_post(post_id: int,
                      post_data: PostCreate,
                      current_user: User = Depends(get_current_user),
                      db: AsyncSession = Depends(get_db)) -> Post:
    post = await db.get(Post, post_id)

    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nie znaleziono posta."
        )

    if post.author_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Tylko autor może edytować post."
        )

    post.title = post_data.title
    post.content = post_data.content

    await db.commit()
    await db.refresh(post)

    return post


@app.patch("/posts/{post_id}", response_model=PostResponse)
async def patch_post(post_id: int,
                     post_data: PostUpdate,
                     current_user: User = Depends(get_current_user),
                     db: AsyncSession = Depends(get_db)) -> Post:
    post = await db.get(Post, post_id)

    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nie znaleziono posta."
        )

    if post.author_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Tylko autor może edytować post."
        )

    updates = post_data.model_dump(exclude_unset=True)

    if not updates:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Nie podano danych do aktualizacji."
        )

    for field, value in updates.items():
        setattr(post, field, value)

    await db.commit()
    await db.refresh(post)

    return post


@app.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post_id: int,
                      current_user: User = Depends(get_current_user),
                      db: AsyncSession = Depends(get_db)) -> None:
    post = await db.get(Post, post_id)

    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nie znaleziono posta."
        )

    if post.author_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Tylko autor może usunąć post."
        )

    await db.delete(post)
    await db.commit()


@app.post("/posts/{post_id}/summarize", response_model=PostSummaryResponse)
async def summarize_existing_post(post_id: int,
                                  db: AsyncSession = Depends(get_db)):
    post = await db.get(Post, post_id)

    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nie znaleziono posta."
        )

    summary = await summarize_post(post.title, post.content)

    return PostSummaryResponse(
        post_id=post.id,
        summary=summary,
    )


@app.post("/posts/{post_id}/comments", response_model=CommentResponse, status_code=status.HTTP_201_CREATED)
async def create_comment(post_id: int,
                         comment_data: CommentCreate,
                         background_tasks: BackgroundTasks,
                         current_user: User = Depends(get_current_user),
                         db: AsyncSession = Depends(get_db)) -> Comment:
    result = await db.execute(
        select(Post)
        .options(selectinload(Post.author))
        .where(Post.id == post_id)
    )
    post = result.scalar_one_or_none()

    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nie znaleziono posta."
        )

    comment = Comment(
        content=comment_data.content,
        post_id=post_id,
        author_id=current_user.id,
    )

    db.add(comment)
    await db.commit()
    await db.refresh(comment)

    background_tasks.add_task(
        send_comment_email,
        post.author.email,
        post.title,
    )
    background_tasks.add_task(
        analyze_comment_sentiment,
        comment.id,
    )

    return comment


@app.get("/posts/{post_id}/comments", response_model=list[CommentResponse])
async def get_post_comments(post_id: int,
                            db: AsyncSession = Depends(get_db)) -> list[Comment]:
    post = await db.get(Post, post_id)

    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nie znaleziono posta."
        )

    result = await db.execute(
        select(Comment).where(Comment.post_id == post_id)
    )

    return list(result.scalars().all())


@app.get("/comments/{comment_id}", response_model=CommentResponse)
async def get_comment(comment_id: int,
                      db: AsyncSession = Depends(get_db)) -> Comment:
    comment = await db.get(Comment, comment_id)

    if comment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nie znaleziono komentarza."
        )

    return comment


@app.put("/comments/{comment_id}", response_model=CommentResponse)
async def update_comment(comment_id: int,
                         comment_data: CommentCreate,
                         background_tasks: BackgroundTasks,
                         current_user: User = Depends(get_current_user),
                         db: AsyncSession = Depends(get_db)) -> Comment:
    comment = await db.get(Comment, comment_id)

    if comment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nie znaleziono komentarza."
        )

    if comment.author_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Tylko autor może edytować komentarz."
        )

    comment.content = comment_data.content
    comment.sentiment = None

    await db.commit()
    await db.refresh(comment)

    background_tasks.add_task(
        analyze_comment_sentiment,
        comment.id,
    )

    return comment


@app.patch("/comments/{comment_id}", response_model=CommentResponse)
async def patch_comment(comment_id: int,
                        comment_data: CommentUpdate,
                        background_tasks: BackgroundTasks,
                        current_user: User = Depends(get_current_user),
                        db: AsyncSession = Depends(get_db)) -> Comment:
    comment = await db.get(Comment, comment_id)

    if comment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nie znaleziono komentarza."
        )

    if comment.author_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Tylko autor może edytować komentarz."
        )

    updates = comment_data.model_dump(exclude_unset=True)

    if not updates:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Nie podano danych do aktualizacji."
        )

    comment.content = updates["content"]
    comment.sentiment = None

    await db.commit()
    await db.refresh(comment)

    background_tasks.add_task(
        analyze_comment_sentiment,
        comment.id,
    )

    return comment


@app.delete("/comments/{comment_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_comment(comment_id: int,
                         current_user: User = Depends(get_current_user),
                         db: AsyncSession = Depends(get_db)) -> None:
    comment = await db.get(Comment, comment_id)

    if comment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nie znaleziono komentarza."
        )

    if comment.author_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Tylko autor może usunąć komentarz."
        )

    await db.delete(comment)
    await db.commit()


@app.get("/posts/{post_id}/with-comments", response_model=PostWithCommentsResponse)
async def get_post_with_comments(post_id: int,
                                 db: AsyncSession = Depends(get_db)) -> Post:
    result = await db.execute(
        select(Post)
        .options(selectinload(Post.comments))
        .where(Post.id == post_id)
    )
    post = result.scalar_one_or_none()

    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nie znaleziono posta."
        )

    return post