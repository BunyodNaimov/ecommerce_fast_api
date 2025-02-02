from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from apps.categories.response_model import CategoryResponseModel
from apps.categories.schemas import CreateCategorySchema
from apps.categories.services import CategoryService
from config.database.session import get_db

router = APIRouter()


@router.post("/", response_model=CategoryResponseModel)
def create_category(category: CreateCategorySchema,
                    db: Session = Depends(get_db)):
    return CategoryService(db, category).create_category()

@router.get("/", response_model=List[CategoryResponseModel])
def get_categories(db: Session = Depends(get_db)):
    return CategoryService(db).get_all_categories()