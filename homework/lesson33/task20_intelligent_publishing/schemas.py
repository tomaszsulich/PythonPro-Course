from typing import Annotated

from pydantic import BaseModel, ConfigDict, EmailStr, StringConstraints


UserName = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        min_length=1,
        max_length=100,
    ),
]

PostTitle = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        min_length=1,
        max_length=200,
    ),
]

Content = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        min_length=1,
        max_length=10_000,
    ),
]


class UserCreate(BaseModel):
    name: UserName
    email: EmailStr


class UserUpdate(BaseModel):
    name: UserName | None = None
    email: EmailStr | None = None


class UserResponse(UserCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)


class UserCreateResponse(UserResponse):
    api_key: str


class PostCreate(BaseModel):
    title: PostTitle
    content: Content


class PostUpdate(BaseModel):
    title: PostTitle | None = None
    content: Content | None = None


class PostResponse(PostCreate):
    id: int
    author_id: int

    model_config = ConfigDict(from_attributes=True)


class CommentCreate(BaseModel):
    content: Content


class CommentUpdate(BaseModel):
    content: Content | None = None


class CommentResponse(CommentCreate):
    id: int
    post_id: int
    author_id: int
    sentiment: str | None

    model_config = ConfigDict(from_attributes=True)


class PostWithCommentsResponse(PostResponse):
    comments: list[CommentResponse]


class PostSummaryResponse(BaseModel):
    post_id: int
    summary: str