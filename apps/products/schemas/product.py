from fastapi.openapi.models import Schema


class ProductSchema(Schema):
    id: int
    name: str

class CreateProductSchema(Schema):
    name: str
    price: float
    category_id: int

    class Config:
        from_attributes = True
