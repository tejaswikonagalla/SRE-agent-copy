from fastapi import status
from app.tests.conftest import client, temp_db
from app.main import app  # Ensure the app is imported for the client to use

@temp_db
def test_items(client):
    response = client.get("/items")

    assert response.status_code == status.HTTP_200_OK

    json = response.json()
    assert isinstance(json, list)  # Ensure the response is a list
    assert len(json) == 3

@temp_db
def test_item(client):
    item_id = "e7d35224-0f51-a62a-25af-4d5c930d9085"
    response = client.get(f"/items/{item_id}")

    assert response.status_code == status.HTTP_200_OK

    json = response.json()
    assert isinstance(json, dict)  # Ensure the response is a dictionary
    assert json.get("name") == "Item3"