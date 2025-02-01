from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config.database.session import Base

class Category(Base):
    """
    Модель категории продуктов.
    """
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)  # Уникальный идентификатор
    name = Column(String, nullable=False, unique=True)  # Название категории
    description = Column(String, nullable=True)  # Описание категории

    products = relationship("Product", back_populates="category")

    def __repr__(self):
        return f"<Category {self.name}>"
