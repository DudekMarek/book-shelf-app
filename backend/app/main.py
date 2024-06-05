from fastapi import FastAPI

# Models import
from database import Base, engine
from models.author_model import AuthorModel
from models.book_model import BookModel
from models.category_model import CategoryModel

# routers import
from routers.category_router import category_router

app = FastAPI()

app.include_router(category_router, prefix="/categories")


def create_tables():
    Base.metadata.create_all(bind=engine)


@app.on_event("startup")
async def startup_event():
    create_tables()


@app.get("/")
async def get_root():
    return {"message": "api is working"}
