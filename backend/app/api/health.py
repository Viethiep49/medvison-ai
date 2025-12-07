"""
Health check endpoints
"""

from fastapi import APIRouter
from app.core.config import settings

router = APIRouter()


@router.get("/health")
async def health_check():
    """Basic health check"""
    return {
        "status": "healthy",
        "service": settings.PROJECT_NAME,
        "version": settings.VERSION
    }


@router.get("/ready")
async def readiness_check():
    """Readiness check - includes model loading status"""
    from app.services.model_service import ModelService

    return {
        "status": "ready" if ModelService.is_loaded() else "not_ready",
        "model_loaded": ModelService.is_loaded(),
        "device": settings.DEVICE
    }
