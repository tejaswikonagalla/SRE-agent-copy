from fastapi import status
from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_root():
    response = client.get("/")

    assert response.status_code == status.HTTP_200_OK

    json_response = response.json()
    assert json_response == {"ping": "pong"}