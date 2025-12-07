"""
Prediction database model
"""

from sqlalchemy import Column, String, Float, DateTime, JSON
from sqlalchemy.sql import func
from app.models.database import Base


class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(String, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    patient_id = Column(String, index=True, nullable=True)

    # Predictions
    predictions = Column(JSON, nullable=False)  # Disease probabilities
    bounding_boxes = Column(JSON, nullable=True)  # Localization results

    # Metadata
    model_version = Column(String, nullable=False)
    confidence_score = Column(Float, nullable=True)
    processing_time = Column(Float, nullable=True)  # seconds

    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # File paths
    image_path = Column(String, nullable=True)
    result_image_path = Column(String, nullable=True)
