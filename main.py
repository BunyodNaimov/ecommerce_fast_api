from fastapi import FastAPI

from config.database.session import Base, engine

app = FastAPI()


# Функция для создания таблиц в базе данных при запуске приложения
def create_tables():
    Base.metadata.create_all(bind=engine)

# Выполняем создание таблиц при запуске сервера
@app.on_event("startup")
def on_startup():
    create_tables()


@app.get("/")
def read_root():
    return {"message": "PostgreSQL подключен!"}