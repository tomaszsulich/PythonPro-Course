from pydantic import BaseModel, ConfigDict


class AuthorCreate(BaseModel):
    name: str


class AuthorResponse(AuthorCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)


class BookCreate(BaseModel):
    title: str
    author: str


class BookResponse(BookCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)


class AuthorBooksResponse(AuthorResponse):
    books: list[BookResponse]