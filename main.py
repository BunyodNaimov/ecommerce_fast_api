from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from apps.products.routers import router as product_router
from apps.categories.routers import router as category_router

app = FastAPI()


# Подключаем роутер для продуктов
app.include_router(product_router, prefix="/products", tags=["products"])
app.include_router(category_router, prefix="/categories", tags=["categories"])


# Отдача статических файлов
app.mount("/static", StaticFiles(directory="apps/static"), name="static")