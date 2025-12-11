from fastapi import FastAPI, status
from fastapi.testclient import TestClient
from app.main import app  # Import the FastAPI app from main.py

client = TestClient(app)

def test_root():
    response = client.get("/")

    assert response.status_code == status.HTTP_200_OK

    json_response = response.json()
    assert json_response == {"ping": "pong"}