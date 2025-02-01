from decouple import config  # Чтение переменных окружения из .env
from sqlalchemy import create_engine # Создание движка для работы с базой
from sqlalchemy.orm import sessionmaker, declarative_base # Создание сессий и базового класса моделей
from  config.settings import settings

## Создаем движок SQLAlchemy для подключения к PostgreSQL
engine = create_engine(settings.DATABASE_URL)

# Создаем сессию для работы с базой
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Базовый класс для всех моделей
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()