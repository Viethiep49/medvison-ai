"""
Application Configuration
"""

from typing import List
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Project Info
    PROJECT_NAME: str = "MedVision AI"
    VERSION: str = "0.1.0"
    DESCRIPTION: str = "AI-powered Chest X-ray Analysis System"

    # API Settings
    API_V1_PREFIX: str = "/api/v1"
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:8501"]

    # Model Settings
    MODEL_PATH: str = "../models/checkpoints/best_model.pth"
    MODEL_TYPE: str = "improved"  # base, lora, improved
    DEVICE: str = "cuda"  # cuda or cpu

    # Image Processing
    IMAGE_SIZE: int = 224
    MAX_IMAGE_SIZE: int = 10 * 1024 * 1024  # 10MB
    ALLOWED_EXTENSIONS: List[str] = [".jpg", ".jpeg", ".png", ".dcm"]

    # Database
    DATABASE_URL: str = "postgresql://medvision:password@localhost:5432/medvision_db"

    # Redis Cache
    REDIS_URL: str = "redis://localhost:6379/0"
    CACHE_EXPIRE: int = 3600  # 1 hour

    # File Storage
    UPLOAD_DIR: str = "../data/uploads"
    PROCESSED_DIR: str = "../data/processed"

    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FILE: str = "../logs/app.log"

    # Security
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 hours

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
