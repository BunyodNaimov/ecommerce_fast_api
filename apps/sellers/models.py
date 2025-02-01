from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config.database.session import Base

class Seller(Base):
    """
    Модель продавца.
    """
    __tablename__ = "sellers"

    id = Column(Integer, primary_key=True, index=True)  # Уникальный идентификатор
    name = Column(String, nullable=False, unique=True)  # Имя продавца
    email = Column(String, nullable=False, unique=True)  # Email продавца
    phone = Column(String, nullable=True)  # Контактный телефон

    products = relationship("Product", back_populates="seller")

    def __repr__(self):
        return f"<Seller {self.name}>"
