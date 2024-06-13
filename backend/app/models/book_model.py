from sqlalchemy import String, Integer, Column, ForeignKey

from app.database import Base


class BookModel(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(Integer, ForeignKey("author.id"), index=True)
    category = Column(Integer, ForeignKey("category.id"), index=True)
    published_year = Column(Integer)
    description = Column(String)
