from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from apps.products.routers import router as product_router

app = FastAPI()


# Подключаем роутер для продуктов
app.include_router(product_router)


# Отдача статических файлов
app.mount("/static", StaticFiles(directory="apps/static"), name="static")