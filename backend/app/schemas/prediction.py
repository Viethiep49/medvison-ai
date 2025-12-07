"""
Prediction schemas
"""

from pydantic import BaseModel, Field
from typing import Dict, List, Optional
from datetime import datetime


class BoundingBox(BaseModel):
    """Bounding box coordinates"""
    x_min: float
    y_min: float
    x_max: float
    y_max: float
    confidence: float
    label: str


class DiseasePrediction(BaseModel):
    """Individual disease prediction"""
    disease: str
    probability: float = Field(..., ge=0.0, le=1.0)
    threshold: float = 0.5
    positive: bool


class PredictionResponse(BaseModel):
    """Prediction API response"""
    prediction_id: str
    filename: str

    # Results
    diseases: List[DiseasePrediction]
    bounding_boxes: Optional[List[BoundingBox]] = None

    # Metadata
    model_version: str
    confidence_score: float
    processing_time: float
    timestamp: datetime

    # Summary
    detected_conditions: List[str]
    risk_level: str  # low, medium, high


class PredictionRequest(BaseModel):
    """Prediction request parameters"""
    patient_id: Optional[str] = None
    threshold: float = Field(default=0.5, ge=0.0, le=1.0)
    include_visualization: bool = True
