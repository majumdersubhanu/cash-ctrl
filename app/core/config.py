from pydantic import computed_field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENVIRONMENT: str = "dev"

    DEV_DATABASE_URL: str = "sqlite+aiosqlite:///./cashctrl.db"
    PROD_DATABASE_URL: str | None = None

    REDIS_URL: str = "redis://localhost:6379/0"

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
