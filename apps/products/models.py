from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Numeric
from sqlalchemy.orm import relationship
from datetime import datetime
from config.database.session import Base
from apps.categories.models import Category
from apps.sellers.models import Seller

class Product(Base):
    """
    Модель продукта, связанная с категорией и продавцом.
    """
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)  # Уникальный идентификатор
    name = Column(String, nullable=False)  # Название продукта
    description = Column(String, nullable=True)  # Описание продукта
    price = Column(Numeric(10, 2), nullable=False)  # Цена продукта
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="SET NULL"), nullable=True)  # Категория
    seller_id = Column(Integer, ForeignKey("sellers.id", ondelete="CASCADE"), nullable=True)  # Продавец
    quantity_stock = Column(Integer, default=0)  # Количество на складе
    is_active = Column(Boolean, default=True)  # Доступность товара
    image_url = Column(String)  # Путь к изображению на диске
    created_at = Column(DateTime, default=datetime.utcnow)  # Дата создания
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # Дата обновления

    category = relationship("Category", back_populates="products")
    seller = relationship("Seller", back_populates="products")
    attributes = relationship("ProductAttribute", back_populates="product", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Product {self.name}, Price: {self.price}, Category ID: {self.category_id}, Seller ID: {self.seller_id}>"

class ProductAttribute(Base):
    """
    Модель для хранения уникальных атрибутов товара.
    """
    __tablename__ = "product_attributes"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"))  # Связь с продуктом
    name = Column(String, nullable=False)  # Название атрибута (например, "Размер", "Бренд")
    value = Column(String, nullable=False)  # Значение атрибута (например, "M", "Apple")

    product = relationship("Product", back_populates="attributes")

    def __repr__(self):
        return f"<ProductAttribute {self.name}: {self.value}>"
