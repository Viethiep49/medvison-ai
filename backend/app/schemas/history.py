"""
History schemas
"""

from pydantic import BaseModel
from typing import Dict, List, Optional
from datetime import datetime


class PredictionHistory(BaseModel):
    """Prediction history record"""
    prediction_id: str
    filename: str
    patient_id: Optional[str]

    predictions: Dict[str, float]
    detected_conditions: List[str]

    model_version: str
    confidence_score: float
    processing_time: float

    created_at: datetime

    class Config:
        from_attributes = True
