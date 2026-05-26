from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """Application settings."""
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    
    # Database settings
    DATABASE_URL: SecretStr

    # Redis settings
    REDIS_URL: SecretStr
    REDIS_CACHE_TTL: int = 86400  # Cache time-to-live in seconds

    APP_NAME: str = "Pro URL Shortener"
    BASE_URL: str = "http://localhost:8000"

    
settings = Settings()  # pyright: ignore[reportCallIssue]