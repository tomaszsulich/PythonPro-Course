from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel


router = APIRouter(prefix="/books", tags=["Books"])

books: dict[int, dict[str, str | int]] = {}


class Book(BaseModel):
    title: str
    author: str


@router.get("")
async def get_books() -> list[dict[str, str | int]]:
    return list(books.values())


@router.get("/{book_id}")
async def get_book(book_id: int) -> dict[str, str | int]:
    if book_id not in books:
        raise HTTPException(
            status_code=404,
            detail="Nie znaleziono książki."
        )

    return books[book_id]


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_book(book: Book) -> dict[str, str | int]:
    book_id = max(books, default=0) + 1

    book_data = {
        "id": book_id,
        "title": book.title,
        "author": book.author
    }

    books[book_id] = book_data
    return book_data


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    if book_id not in books:
        raise HTTPException(
            status_code=404,
            detail="Nie znaleziono książki."
        )

    del books[book_id]