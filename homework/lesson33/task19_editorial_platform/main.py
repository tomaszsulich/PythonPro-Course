from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import (
    BackgroundTasks,
    Depends,
    FastAPI,
    Header,
    HTTPException,
    status,
)
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from database import Base, engine, get_db
from models import Comment, Post, User
from schemas import (
    CommentCreate,
    CommentResponse,
    PostCreate,
    PostResponse,
    PostWithCommentsResponse,
    UserCreate,
    UserResponse,
)
from tasks import send_comment_email


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None]:
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)

    yield

    await engine.dispose()


app = FastAPI(lifespan=lifespan)


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


@app.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user_data: UserCreate,
                      db: AsyncSession = Depends(get_db)) -> User:
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

    user.name = user_data.name
    user.email = user_data.email

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


@app.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post_id: int,
                      db: AsyncSession = Depends(get_db)) -> None:
    post = await db.get(Post, post_id)

    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nie znaleziono posta."
        )

    await db.delete(post)
    await db.commit()


@app.post("/posts/{post_id}/comments", response_model=CommentResponse, status_code=status.HTTP_201_CREATED)
async def create_comment(post_id: int,
                         comment_data: CommentCreate,
                         background_tasks: BackgroundTasks,
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
    )

    db.add(comment)
    await db.commit()
    await db.refresh(comment)

    background_tasks.add_task(
        send_comment_email,
        post.author.email,
        post.title,
    )

    return comment


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