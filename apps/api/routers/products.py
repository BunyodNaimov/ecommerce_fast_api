from typing import List

from fastapi import APIRouter, Depends, HTTPException, Request, Query
from sqlalchemy.orm import Session

from apps.products.schemas.product import ProductSchema, CreateProductSchema
from apps.products.services.product import ProductService
from config.database.session import get_db


router = APIRouter()


@router.get("/", response_model=List[ProductSchema])
def get_all_products(db: Session = Depends(get_db)):
    return ProductService(db).get_all_products()


@router.post("/", response_model=ProductSchema)
def create_product(product: CreateProductSchema,
                   db: Session = Depends(get_db)):
    return ProductService(db).create_product(product)