from fastapi import FastAPI, status
from fastapi.testclient import TestClient
from app.main import app  # Import the FastAPI app from main.py

client = TestClient(app)

def test_root():
    # Ensure the database is migrated before running the test
    from app.db import Base, engine
    Base.metadata.create_all(bind=engine)

    # Use a valid hostname or IP address for testing
    response = client.get("/")

    assert response.status_code == status.HTTP_200_OK

    json_response = response.json()
    assert json_response == {"ping": "pong"}