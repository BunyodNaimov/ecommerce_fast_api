from sqlalchemy.orm import Session

from apps.categories.models import Category
from apps.categories.schemas import CreateCategorySchema


class CategoryService:
    def __init__(self, db: Session, data: CreateCategorySchema=None):
        self.db = db
        self.data = data

    def create_category(self):
        obj = Category(name=self.data.name)
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def get_all_categories(self):
        categories = self.db.query(Category).all()
        return categories