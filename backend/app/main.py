"""
MedVision AI - Main FastAPI Application
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api import health, predict, history

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="AI-powered Chest X-ray Analysis System",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health.router, prefix="/api", tags=["health"])
app.include_router(predict.router, prefix="/api", tags=["prediction"])
app.include_router(history.router, prefix="/api", tags=["history"])


@app.on_event("startup")
async def startup_event():
    """Load model on startup"""
    from app.services.model_service import ModelService
    ModelService.load_model()


@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown"""
    pass


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
