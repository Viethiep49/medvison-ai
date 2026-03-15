import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Define database URL (using local SQLite for MVP)
# A local file named 'medvision.db' will be created in the backend folder
DB_URL = "sqlite:///./medvision.db"

# Create the SQLAlchemy engine
# connect_args={"check_same_thread": False} is required for SQLite across multiple requests in FastAPI
engine = create_engine(DB_URL, connect_args={"check_same_thread": False})

# Create a customized Session class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative class definitions
Base = declarative_base()

# Dependency for FastAPI to get DB sessions
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
