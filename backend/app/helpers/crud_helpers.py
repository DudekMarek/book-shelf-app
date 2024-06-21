from fastapi import HTTPException
from sqlalchemy.orm import Session


def get_items(model, db: Session, limit: int = 10):
    items = db.query(model).all()
    return items[0:limit]


def get_item(model, db: Session, item_id: int):
    item = db.query(model).filter(model.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail=f"{model} not found")
    return item


def create_item(model, schema, db: Session):
    db_item = model
    pass


def update_item(model, item_id: int, schema, db: Session):
    db_item = db.query(model).filter(model.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail=f"{model} not found")

    for key, value in schema.model_dump().items():
        setattr(db_item, key, value)

    db.commit()
    db.refresh(db_item)
    return db_item
