from typing import Optional

from aiohttp import ClientSession
from loguru import logger
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

logger.add(
    "src/logs/debug.log",
    format="{time} - {level} - {message}",
    level="INFO",
    rotation="5 MB",
    compression="zip"
)


class RedisSettings(BaseSettings):
    redis_host: str = Field(json_schema_extra={'env': 'REDIS_HOST'})
    redis_port: str = Field(json_schema_extra={'env': 'REDIS_PORT'})
    redis_user: str = Field(json_schema_extra={'env': 'REDIS_USER'})
    redis_password: str = Field(json_schema_extra={'env': 'REDIS_PASSWORD'})
    redis_user_password: str = Field(json_schema_extra={'env': 'REDIS_USER_PASSWORD'})

    model_config = SettingsConfigDict(env_prefix="REDIS_", env_file=".env", extra="ignore")


class Settings(BaseSettings):
    app_port: int = Field(json_schema_extra={'env': 'APP_PORT'})

    redis: RedisSettings

    model_config = SettingsConfigDict(env_prefix="APP_", env_file=".env", extra="ignore")


class SessionManager:
    _session: ClientSession | None = None

    @classmethod
    async def get_session(cls) -> ClientSession:
        """Возвращает сессию aiohttp, создавая её при первом вызове."""
        if cls._session is None or cls._session.closed:
            cls._session = ClientSession()
        return cls._session

    @classmethod
    async def close_session(cls):
        """Закрывает сессию, если она существует."""
        if cls._session is not None:
            await cls._session.close()
            cls._session = None


settings = Settings(
    redis=RedisSettings(),
)
