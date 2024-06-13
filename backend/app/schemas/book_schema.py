from pydantic import BaseModel, Field

from .author_schema import AuthorSchema
from .category_schema import CategorySchema


class BookSchema(BaseModel):
    title: str = Field(min_length=4)
    author: AuthorSchema
    category: CategorySchema
    published_date: int = Field(ge=-1000, le=2020)
    description: str
