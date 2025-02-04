from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

from apps.products.services.product import ProductService
from config.database.session import get_db

router = APIRouter()
templates = Jinja2Templates(directory="apps/web/templates")


@router.get("/", response_class=HTMLResponse) # Сделаем путь /web/products/
def get_products(request: Request, db: Session = Depends(get_db)):
    products = ProductService(db).get_all_products()
    return templates.TemplateResponse("products/products.html", {"request": request, "products": products})

