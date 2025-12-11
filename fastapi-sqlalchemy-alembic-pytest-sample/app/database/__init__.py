from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

# Use an environment variable for the database URL if available, otherwise default to the example URL
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)