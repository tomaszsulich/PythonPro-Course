from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import Literal

from fastapi import Depends, FastAPI, HTTPException, Query, status
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


@app.post("/books", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
async def create_book(book_data: BookCreate, db: AsyncSession = Depends(get_db)) -> Book:
    book = Book(**book_data.model_dump())

    db.add(book)
    await db.commit()
    await db.refresh(book)

    return book


@app.get("/books", response_model=list[BookResponse])
async def get_books(skip: int = Query(default=0, ge=0),
                    limit: int = Query(default=10, ge=1, le=100),
                    category: str | None = Query(default=None, min_length=1),
                    min_price: float | None = Query(default=None, ge=0),
                    max_price: float | None = Query(default=None, ge=0),
                    sort_by: Literal["price", "title"] | None = None,
                    sort_order: Literal["asc", "desc"] | None = "asc",
                    db: AsyncSession = Depends(get_db)) -> list[Book]:
    if category is not None:
        category = category.strip()

        if not category:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Kategoria nie może być pusta."
            )

    if (
        min_price is not None
        and max_price is not None
        and min_price > max_price
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Minimalna cena nie może być większa od maksymalnej."
        )

    query = select(Book)

    if category is not None:
        query = query.where(Book.category == category)

    if min_price is not None:
        query = query.where(Book.price >= min_price)

    if max_price is not None:
        query = query.where(Book.price <= max_price)

    if sort_by == "price":
        sort_column = Book.price
    elif sort_by == "title":
        sort_column = Book.title
    else:
        sort_column = None

    if sort_column is not None:
        if sort_order == "desc":
            query = query.order_by(sort_column.desc())
        else:
            query = query.order_by(sort_column.asc())

    query = query.offset(skip).limit(limit)
    result = await db.execute(query)

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