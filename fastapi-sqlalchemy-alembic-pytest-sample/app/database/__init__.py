from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine
import os

# Use an environment variable for the database URL if available, otherwise default to the example URL
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative class definitions
Base = declarative_base()

# Ensure the directory structure is correct and __init__.py files are present
# Create a minimal __init__.py file in the app and database directories if they don't exist
# This is necessary for Python to recognize these directories as packages