from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine

# Updated to use a valid SQLite URL format
DATABASE_URL = "sqlite:///test.db"  # Example database URL

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()