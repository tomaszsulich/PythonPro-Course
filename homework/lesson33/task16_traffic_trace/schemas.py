from pydantic import BaseModel, ConfigDict


class BookCreate(BaseModel):
    title: str
    author: str


class BookResponse(BookCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)