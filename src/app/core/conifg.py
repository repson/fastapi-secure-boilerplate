from typing import Any, Dict, List, Optional, Union

from pydantic import BaseSettings, Field, PostgresDsn, validator, AnyHttpUrl


class Settings(BaseSettings):
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SERVER_NAME: str
    SERVER_HOST: AnyHttpUrl
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    PROJECT_NAME: str
    API_PREFIX: str = "/api"
    VERSION: str = "0.1.0"
    DEBUG: bool = False