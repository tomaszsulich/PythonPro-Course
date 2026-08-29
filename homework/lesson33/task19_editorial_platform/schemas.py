from pydantic import BaseModel, ConfigDict, EmailStr


class UserCreate(BaseModel):
    name: str
    email: EmailStr


class UserResponse(UserCreate):
    id: int
    api_key: str

    model_config = ConfigDict(from_attributes=True)


class PostCreate(BaseModel):
    title: str
    content: str


class PostResponse(PostCreate):
    id: int
    author_id: int

    model_config = ConfigDict(from_attributes=True)


class CommentCreate(BaseModel):
    content: str


class CommentResponse(CommentCreate):
    id: int
    post_id: int

    model_config = ConfigDict(from_attributes=True)


class PostWithCommentsResponse(PostResponse):
    comments: list[CommentResponse]