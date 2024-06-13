from fastapi import FastAPI

from contextlib import asynccontextmanager

# Models import
from app.database import Base, engine
from app.models.author_model import AuthorModel
from app.models.book_model import BookModel
from app.models.category_model import CategoryModel

# routers import
from app.routers.category_router import category_router


def create_tables():
    Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(category_router, prefix="/categories")


@app.get("/")
async def get_root():
    return {"message": "api is working"}
