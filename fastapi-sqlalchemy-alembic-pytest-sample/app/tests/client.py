from fastapi import Header, HTTPException, status
from fastapi.testclient import TestClient

from app.dependencies import get_database
from app.main import app
from app.database import SessionLocal  # Import SessionLocal from the correct module


def temp_db(f):
    def func(*args, **kwargs):
        def override_get_db():
            db = SessionLocal()
            try:
                yield db
            finally:
                db.close()

        app.dependency_overrides[get_database] = override_get_db
        try:
            f(*args, **kwargs)
        finally:
            app.dependency_overrides[get_database] = get_database

    return func


client = TestClient(app)