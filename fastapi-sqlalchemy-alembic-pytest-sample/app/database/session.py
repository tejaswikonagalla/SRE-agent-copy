import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

# Ensure the environment variable is set, or provide a default for development
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

# Correctly handle the case where DATABASE_URL might be incorrectly set
if not SQLALCHEMY_DATABASE_URL.startswith(("sqlite://", "postgresql://", "mysql://", "oracle://", "mssql://")):
    raise ValueError("Invalid DATABASE_URL. Ensure it starts with a valid database dialect.")

# Use StaticPool for SQLite to avoid issues with multiple threads in testing environments
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False} if "sqlite" in SQLALCHEMY_DATABASE_URL else {},
    poolclass=StaticPool if "sqlite" in SQLALCHEMY_DATABASE_URL else None,
    pool_pre_ping=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()