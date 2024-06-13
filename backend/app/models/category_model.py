from sqlalchemy import String, Integer, Column

from app.database import Base


class CategoryModel(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
