import uuid
from datetime import datetime
from sqlalchemy import Column, String, Integer, Float, Text, JSON, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base

class Scan(Base):
    __tablename__ = "scans"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    patient_name = Column(String, nullable=True)
    patient_age = Column(Integer, nullable=True)
    patient_gender = Column(String, nullable=True)
    
    image_path = Column(String, nullable=False)
    status = Column(String, nullable=False, default="processing")
    doctor_notes = Column(Text, nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    findings = relationship("ScanFinding", back_populates="scan", cascade="all, delete-orphan")
    messages = relationship("ChatMessage", back_populates="scan", cascade="all, delete-orphan")


class ScanFinding(Base):
    __tablename__ = "scan_findings"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    scan_id = Column(String, ForeignKey("scans.id", ondelete="CASCADE"), nullable=False)
    
    disease_name = Column(String, nullable=False)
    confidence_score = Column(Float, nullable=False)
    
    # Store coordinates: {"x": 10, "y": 20, "w": 30, "h": 40}
    # SQLAlchemy mapped JSON handles SQLite elegantly.
    bounding_box = Column(JSON, nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)

    # Back reference
    scan = relationship("Scan", back_populates="findings")


class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    scan_id = Column(String, ForeignKey("scans.id", ondelete="CASCADE"), nullable=False)
    
    # E.g., 'user' (Doctor), 'assistant' (LLM), 'system'
    role = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    
    created_at = Column(DateTime, default=datetime.utcnow)

    # Back reference
    scan = relationship("Scan", back_populates="messages")
