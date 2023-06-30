import secrets
import logging

from pathlib import Path
from typing import Any, Dict, List, Optional, Union
from pydantic import BaseSettings, Field, PostgresDsn, validator, AnyHttpUrl, HttpUrl, EmailStr

ROOT_DIR: Path = Path(__file__).parent.parent.parent,resove()

class Settings(BaseSettings):

    TITLE: str = "FastAPI"
    DESCRIPTION: str = "FastAPI Boilerplate"
    VERSION: str = "0.1.0"
    DEBUG: bool = True

    SERVER_HOST: str = "http://localhost:8000"
    SERVER_PORT: int = 8000
    SERVER_WORKERS: int = 1
    API_PREFIX: str = "/api/v1"
    DOCS_URL: str = "/docs"
    OPENAPI_URL: str = "/openapi.json"
    REDOC_URL: Optional[str] = "/redoc"
    OPENAPI_PREFIX: str = ""

    SECURITY_BCRYPT_ROUNDS: int = 12
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8 * 2
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    IS_ALLOWED_CREDENTIALS: bool = False
    ALLOWED_HOSTS: List[str] = ["*"]

    LOGGING_LEVEL: int = logging.DEBUG
    LOGGERS: Tuple[str, str] = ("uvicorn.asgi", "uvicorn.access")

    DEFAULT_DATABASE_URI: str = "sqlite:///./app.db"
    DEFAULT_DATABASE_NAME: str = "app.db"
    DEFAULT_DATABASE_DRIVER: str = "sqlite" 

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"

settings: Settings = Settings()