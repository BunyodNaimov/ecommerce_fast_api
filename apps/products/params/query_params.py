from pydantic import BaseModel


class CreateProductQueryParams(BaseModel):
    name: str
    price: float
    category_id: int