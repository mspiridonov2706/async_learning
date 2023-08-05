import os

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')


class PostgresqlSettings(BaseConfig):
    model_config = SettingsConfigDict(env_prefix='POSTGRES_', case_sensitive=False)

    user: str = Field(default=...)
    password: str = Field(default=...)
    db: str = Field(default=...)
    port: int = Field(default=...)
    host: str = Field(default=...)


class Settings(BaseConfig):
    postgres: PostgresqlSettings = PostgresqlSettings()


settings = Settings()

# Корень проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
