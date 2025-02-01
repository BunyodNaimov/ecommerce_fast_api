from typing import List

from fastapi import APIRouter, UploadFile, File, Depends, HTTPException, Request, Query
import os
from config import settings
from . import services
from sqlalchemy.orm import Session
from config.database.session import get_db
from .params.query_params import CreateProductQueryParams
from .schemas.product import ProductSchema, CreateProductSchema
from .services.product import ProductService

router = APIRouter()


@router.get("/products", response_model=List[ProductSchema])
def get_all_products(db: Session = Depends(get_db)):
    return ProductService(db).get_all_products()


@router.post("/")
def create_product(product: CreateProductSchema,
                   db: Session = Depends(get_db)):
    return ProductService(db).create_product(product)


# Папка для хранения изображений
IMAGE_DIR = "media/products"


@router.post("/{product_id}/upload-image/")
async def upload_product_image(
        product_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)
):
    """
    Загружает изображение для товара.

    Args:
        product_id (int): ID товара.
        file (UploadFile): Файл изображения.
        db (Session): Сессия базы данных.

    Returns:
        dict: Сообщение об успешной загрузке.
    """
    # Проверяем, существует ли товар
    product = services.get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Товар не найден")

    # Создаем папку, если её нет
    os.makedirs(IMAGE_DIR, exist_ok=True)

    # Генерируем уникальное имя файла
    file_extension = file.filename.split(".")[-1]
    filename = f"product_{product_id}.{file_extension}"
    file_path = os.path.join(IMAGE_DIR, filename)

    # Сохраняем файл на диск
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # Обновляем путь к изображению в базе данных
    product.image_url = f"/media/products/{filename}"
    db.commit()
    db.refresh(product)

    return {"message": "Изображение успешно загружено", "image_url": product.image_url}
