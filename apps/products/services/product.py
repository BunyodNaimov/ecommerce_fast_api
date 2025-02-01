from sqlalchemy.orm import Session

from apps.products.models import Product
from apps.products.schemas.product import CreateProductSchema


class ProductService:

    def __init__(self, db: Session):
        self.db = db
    def get_all_products(self):
        return self.db.query(Product).all()

    def create_product(self, product_data: CreateProductSchema):
        """Создает новый продукт и сохраняет его в базе данных."""
        new_product = Product(
            name=product_data.name,
            price=product_data.price,
            category_id=product_data.category_id
        )
        self.db.add(new_product)
        self.db.commit()
        self.db.refresh(new_product)  # Обновляем объект из базы данных
        return new_product
