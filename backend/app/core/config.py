from pydantic import BaseSettings, AnyHttpUrl
from typing import List

class Settings(BaseSettings):
    ENV: str = "development"
    DEBUG: bool = True

    # Database
    DATABASE_URL: str = "postgresql+asyncpg://postgres:password@db:5432/ai_platform"

    # Qdrant
    QDRANT_URL: str = "http://qdrant:6333"
    QDRANT_API_KEY: str = ""

    # LLM / OpenAI
    OPENAI_API_KEY: str = ""

    # Security
    API_KEY: str = "changeme"

    # CORS
    CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost:3000"]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
