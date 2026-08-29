from fastapi import FastAPI
from routers.authors import router as authors_router
from routers.books import router as books_router


app = FastAPI()

app.include_router(authors_router)
app.include_router(books_router)