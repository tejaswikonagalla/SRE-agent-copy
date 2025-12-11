from fastapi import status
from app.tests.conftest import client, temp_db
from app.models import Group, Item  # Assuming these are the correct models

@temp_db
def test_groups(client, session):
    # Setup test data
    group1 = Group(id="7d60e1d4-a6af-fc52-6355-67c3094479ab", name="Group1", description="Group1 description")
    group2 = Group(id="218587ed-d548-bd06-d278-43583021c1a9", name="Group2", description="Group2 description")
    session.add_all([group1, group2])
    session.commit()

    response = client.get("/groups")

    assert response.status_code == status.HTTP_200_OK

    json = response.json()
    assert len(json) == 2

@temp_db
def test_group(client, session):
    # Setup test data
    group = Group(id="218587ed-d548-bd06-d278-43583021c1a9", name="Group2", description="Group2 description")
    session.add(group)
    session.commit()

    response = client.get(f"/groups/{group.id}")

    assert response.status_code == status.HTTP_200_OK

    json = response.json()
    assert json["name"] == "Group2"
    assert json["description"] == "Group2 description"

@temp_db
def test_group_items_1(client, session):
    # Setup test data
    group = Group(id="7d60e1d4-a6af-fc52-6355-67c3094479ab", name="Group1", description="Group1 description")
    item1 = Item(id="item1", name="Item1", group_id=group.id)
    item2 = Item(id="item2", name="Item2", group_id=group.id)
    session.add_all([group, item1, item2])
    session.commit()

    response = client.get(f"/groups/{group.id}/items")

    assert response.status_code == status.HTTP_200_OK

    json = response.json()
    assert len(json) == 2

@temp_db
def test_group_items_2(client, session):
    # Setup test data
    group = Group(id="218587ed-d548-bd06-d278-43583021c1a9", name="Group2", description="Group2 description")
    item = Item(id="item3", name="Item3", group_id=group.id)
    session.add_all([group, item])
    session.commit()

    response = client.get(f"/groups/{group.id}/items")

    assert response.status_code == status.HTTP_200_OK

    json = response.json()
    assert len(json) == 1