from fastapi import Header, HTTPException, status
from fastapi.testclient import TestClient

from ..dependencies import get_database
from ..main import app
from ..database import SessionLocal  # Import SessionLocal from the correct module


def temp_db(f):
    def func(*args, **kwargs):
        def override_get_db():
            db = SessionLocal()
            try:
                yield db
            finally:
                db.close()

        app.dependency_overrides[get_database] = override_get_db
        f(*args, **kwargs)
        app.dependency_overrides[get_database] = get_database

    return func


client = TestClient(app)