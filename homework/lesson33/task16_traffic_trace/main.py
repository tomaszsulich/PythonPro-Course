import time
import uuid
from collections.abc import AsyncGenerator, Awaitable, Callable
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException, Request, Response, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import Base, engine, get_db
from models import Book
from schemas import BookCreate, BookResponse


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None]:
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)

    yield

    await engine.dispose()


app = FastAPI(lifespan=lifespan)


@app.middleware("http")
async def log_requests(request: Request,
                       call_next: Callable[[Request], Awaitable[Response]]) -> Response:
    request_id = str(uuid.uuid4())
    start_time = time.perf_counter()

    response = await call_next(request)

    duration = time.perf_counter() - start_time

    with open("requests.log", "a", encoding="utf-8") as file:
        file.write(
            f"{request_id} | {request.method} "
            f"{request.url.path} | {duration:.4f} s\n"
        )

    response.headers["X-Request-ID"] = request_id

    return response


@app.post("/books", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
async def create_book(book_data: BookCreate, db: AsyncSession = Depends(get_db)) -> Book:
    book = Book(**book_data.model_dump())

    db.add(book)
    await db.commit()
    await db.refresh(book)

    return book


@app.get("/books", response_model=list[BookResponse])
async def get_books(db: AsyncSession = Depends(get_db)) -> list[Book]:
    result = await db.execute(select(Book))
    return list(result.scalars().all())


@app.get("/books/{book_id}", response_model=BookResponse)
async def get_book(book_id: int, db: AsyncSession = Depends(get_db)) -> Book:
    book = await db.get(Book, book_id)

    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nie znaleziono książki."
        )

    return book


@app.put("/books/{book_id}", response_model=BookResponse)
async def update_book(book_id: int, book_data: BookCreate, db: AsyncSession = Depends(get_db)) -> Book:
    book = await db.get(Book, book_id)

    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nie znaleziono książki."
        )

    book.title = book_data.title
    book.author = book_data.author

    await db.commit()
    await db.refresh(book)

    return book


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int, db: AsyncSession = Depends(get_db)) -> None:
    book = await db.get(Book, book_id)

    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nie znaleziono książki."
        )

    await db.delete(book)
    await db.commit()