from pydantic_settings import BaseSettings
from typing import List
class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    DEBUG: bool
    ALLOWED_HOSTS: List[str]
    class Config:
        env_file = ".env"

settings = Settings()