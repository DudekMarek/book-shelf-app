from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models.category_model import CategoryModel

category_router = APIRouter()


@category_router.get("/")
async def get_categories(db: Session = Depends(get_db)):
    categories = db.query(CategoryModel).all()
    return categories
