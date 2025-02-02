from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from apps.api.routers.products import router as product_router
from apps.api.routers.categories import router as category_router

app = FastAPI()


# Подключаем роутер для продуктов
app.include_router(product_router, prefix="/api/products", tags=["products"])
app.include_router(category_router, prefix="/api/categories", tags=["categories"])


# Отдача статических файлов
# app.mount("/static", StaticFiles(directory="apps/static"), name="static")