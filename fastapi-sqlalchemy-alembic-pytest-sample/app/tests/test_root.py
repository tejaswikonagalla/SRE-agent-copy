from fastapi import status, FastAPI
from fastapi.testclient import TestClient

# Assuming the app is defined in this file for testing purposes
app = FastAPI()

@app.get("/")
async def read_root():
    return {"ping": "pong"}

client = TestClient(app)

def test_root():
    response = client.get("/")

    assert response.status_code == status.HTTP_200_OK

    json_response = response.json()
    assert json_response == {"ping": "pong"}