from sqlalchemy import String, Integer, Column

from database import Base


class AuthorModel(Base):
    __tablename__ = "author"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    birth_year = Column(Integer)
    nationality = Column(String)
