from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.category_model import CategoryModel
from app.schemas.category_schema import CategorySchema

category_router = APIRouter()


@category_router.get("/")
async def get_categories(limit: int = 10, db: Session = Depends(get_db)):
    categories = db.query(CategoryModel).all()
    return categories[0:limit]


@category_router.get("/{category_id}")
async def get_category(category_id: int, db: Session = Depends(get_db)):
    category = db.query(CategoryModel).filter(CategoryModel.id == category_id).first()
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@category_router.post("/")
async def post_category(category: CategorySchema, db: Session = Depends(get_db)):
    db_category = CategoryModel(name=category.name)
    try:
        db.add(db_category)
        db.commit()
        db.refresh(db_category)
        return db_category
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@category_router.put("/{category_id}")
async def update_category(
    category_id: int, category: CategorySchema, db: Session = Depends(get_db)
):
    db_category = (
        db.query(CategoryModel).filter(CategoryModel.id == category_id).first()
    )
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")

    db_category["name"] = category.name
    db.commit()
    db.refresh(db_category)
    return db_category
