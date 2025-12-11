from fastapi import status

from app.tests.conftest import client, temp_db, setup_test_data


@temp_db
def test_items(client):
    setup_test_data()  # Ensure test data is set up before running the test
    response = client.get("/items")

    assert response.status_code == status.HTTP_200_OK

    json = response.json()
    assert len(json) == 3

@temp_db
def test_item(client):
    setup_test_data()  # Ensure test data is set up before running the test
    item_id = "e7d35224-0f51-a62a-25af-4d5c930d9085"
    response = client.get(f"/items/{item_id}")

    assert response.status_code == status.HTTP_200_OK

    json = response.json()
    assert json["name"] == "Item3"