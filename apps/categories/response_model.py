from pydantic import BaseModel


class CategoryResponseModel(BaseModel):
    id: int
    name: str