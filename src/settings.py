import os

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')


class PostgresqlSettings(BaseConfig):
    user: str = Field(default=..., alias="POSTGRES_USER")
    password: str = Field(default=..., alias="POSTGRES_PASSWORD")
    db: str = Field(default=..., alias="POSTGRES_DB")
    port: int = Field(default=..., alias="POSTGRES_PORT")
    host: str = Field(default=..., alias="POSTGRES_HOST")


class Settings(BaseConfig):
    postgres: PostgresqlSettings = PostgresqlSettings()


settings = Settings()

# Корень проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
