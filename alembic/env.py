import os
import sys
from dotenv import load_dotenv
from logging.config import fileConfig
from sqlalchemy import create_engine, pool
from alembic import context
from sqlalchemy.ext.declarative import declarative_base
from config.database.session import Base  # Импортируем Base, который содержит все модели

# Загружаем переменные окружения из .env файла
load_dotenv()

# Получаем строку подключения к базе данных из переменной окружения
DATABASE_URL = os.getenv('DATABASE_URL')

# Создаем engine для подключения к базе данных
engine = create_engine(DATABASE_URL)

# Добавляем путь к проекту в sys.path
sys.path.append(os.getcwd())

# Импортируем Base и модели
from apps.products.models import Product
from apps.categories.models import Category
from apps.sellers.models import Seller

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Пример использования DATABASE_URL в alembic
config.set_section_option('alembic', 'sqlalchemy.url', DATABASE_URL)

# Настройка логгера
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Для поддержки 'autogenerate' нужно указать target_metadata
# Используем Base.metadata, который содержит метаданные всех моделей
target_metadata = Base.metadata

# Функция для запуска миграций в оффлайн-режиме
def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    Здесь конфигурируем контекст с URL базы данных, не создавая Engine.
    Это позволяет выполнять миграции без использования DBAPI.
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

# Функция для запуска миграций в онлайн-режиме
def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    В этом случае создаем Engine и ассоциируем подключение с контекстом.
    """
    connectable = create_engine(DATABASE_URL)

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

# Определение, какой режим используется: оффлайн или онлайн
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
