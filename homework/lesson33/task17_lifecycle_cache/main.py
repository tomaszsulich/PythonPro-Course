import json
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import Base, engine, get_db
from models import Book
from schemas import BookCreate, BookResponse


CACHE_FILE = Path("cache.json")

cache: dict[str, str] = {}


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None]:
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)

    if CACHE_FILE.exists():
        with CACHE_FILE.open("r", encoding="utf-8") as file:
            cache.update(json.load(file))

    yield

    with CACHE_FILE.open("w", encoding="utf-8") as file:
        json.dump(cache, file, ensure_ascii=False, indent=4)

    await engine.dispose()


app = FastAPI(lifespan=lifespan)


@app.get("/cache")
async def get_cache() -> dict[str, str]:
    return cache


@app.put("/cache/{key}")
async def update_cache(key: str, value: str) -> dict[str, str]:
    cache[key] = value
    return cache


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