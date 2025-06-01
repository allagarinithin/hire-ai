from sqlalchemy import Column, Integer, String, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json

Base = declarative_base()

class Candidate(Base):
    __tablename__ = "candidates"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    skills = Column(Text, nullable=False)  # Store as JSON string
    experience = Column(Text, nullable=False)  # Store as JSON string
    education = Column(Text, nullable=False)  # Store as JSON string

# SQLite DB setup
DATABASE_URL = "sqlite:///./candidates.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables
Base.metadata.create_all(bind=engine) 