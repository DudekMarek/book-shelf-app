from pydantic import BaseModel, Field


class AuthorSchema(BaseModel):
    name: str = Field(min_length=4)
    birth_year: int = Field(ge=-1000, le=2020)
    nationality: str = Field(min_length=4)
