from dotenv import load_dotenv
import subprocess
import sys
import os

# Загрузим переменные из .env
load_dotenv()

def run_alembic_command(command):
    """Функция для выполнения команды Alembic"""
    result = subprocess.run(
        ["alembic", *command], capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        sys.exit(1)
    else:
        print(result.stdout)

def main():
    """Основная функция для создания и применения миграций"""
    print("Создание миграции...")
    run_alembic_command(["revision", "--autogenerate", "-m", "Update models"])

    print("Применение миграций...")
    run_alembic_command(["upgrade", "head"])

if __name__ == "__main__":
    main()
