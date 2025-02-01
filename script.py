import os

# Основные директории
directories = [
    "apps",
    "apps/products",
    "apps/categories",
    "apps/sellers",
    "apps/templates",
    "apps/static/styles",
    "apps/static/images",
    "config",
    "config/database",
]

# Файлы, которые нужно создать
files = {
    "apps/__init__.py": "",
    "apps/products/__init__.py": "",
    "apps/products/models.py": "",
    "apps/products/schemas.py": "",
    "apps/products/services.py": "",
    "apps/products/routers.py": "",
    "apps/categories/__init__.py": "",
    "apps/categories/models.py": "",
    "apps/categories/schemas.py": "",
    "apps/categories/services.py": "",
    "apps/categories/routers.py": "",
    "apps/sellers/__init__.py": "",
    "apps/sellers/models.py": "",
    "apps/sellers/schemas.py": "",
    "apps/sellers/services.py": "",
    "apps/sellers/routers.py": "",
    "apps/templates/base.html": "",
    "apps/templates/index.html": "",
    "apps/templates/products/products.html": "",
    "apps/templates/categories/categories.html": "",
    "apps/templates/sellers/sellers.html": "",
    "apps/static/styles/main.css": "",
    "config/__init__.py": "",
    "config/settings.py": "",
    "config/database/__init__.py": "",
    "config/database/session.py": "",
    "main.py": "",
}

# Создание директорий
for directory in directories:
    os.makedirs(directory, exist_ok=True)
    print(f"Создана директория: {directory}")

# Создание файлов
for file_path, content in files.items():
    with open(file_path, "w") as file:
        file.write(content)
    print(f"Создан файл: {file_path}")

print("Структура проекта успешно создана!")