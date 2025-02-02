from pydantic import BaseModel


class ProductSchema(BaseModel):
    id: int
    name: str
    category_id: int


class CreateProductSchema(BaseModel):
    name: str
    price: float
    category_id: int
