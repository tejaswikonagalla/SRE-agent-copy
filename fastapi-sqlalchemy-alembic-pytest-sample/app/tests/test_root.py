from fastapi import FastAPI, status
from fastapi.testclient import TestClient
from app.main import app  # Import the FastAPI app from main.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base  # Assuming there's a database.py with Base defined

# Setup the database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database tables
Base.metadata.create_all(bind=engine)

client = TestClient(app)

def test_root():
    response = client.get("/")

    assert response.status_code == status.HTTP_200_OK

    json_response = response.json()
    assert json_response == {"ping": "pong"}