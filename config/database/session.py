from decouple import config  # Чтение переменных окружения из .env
from sqlalchemy import create_engine # Создание движка для работы с базой
from sqlalchemy.orm import sessionmaker, declarative_base # Создание сессий и базового класса моделей

# Загружаем URL базы данных из .env
DATABASE_URL = config('DATABASE_URL')

## Создаем движок SQLAlchemy для подключения к PostgreSQL
engine = create_engine(DATABASE_URL)

# Создаем сессию для работы с базой
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Базовый класс для всех моделей
Base = declarative_base()