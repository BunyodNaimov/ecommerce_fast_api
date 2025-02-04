from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from apps.api.routers.products import router as api_product_router
from apps.api.routers.categories import router as api_category_router
from apps.web.routers.products import router as web_product_router
app = FastAPI()


# Подключаем роутеры для API
app.include_router(api_product_router, prefix="/api/products", tags=["products"])
app.include_router(api_category_router, prefix="/api/categories", tags=["categories"])

# Подключаем роутеры для веб-страниц
app.include_router(web_product_router, prefix="/web/products", include_in_schema=False)

# Отдача статических файлов
app.mount("/static", StaticFiles(directory="apps/web/static"), name="static")