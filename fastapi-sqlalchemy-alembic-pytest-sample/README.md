# FastAPI SQLAlchemy Alembic Pytest Sample

This project demonstrates a simple setup using FastAPI with SQLAlchemy, Alembic for migrations, and Pytest for testing.

## Project Structure

- `app/`: Contains the main application code.
  - `main.py`: The entry point for the FastAPI application.
  - `database/`: Contains database setup and session management.
    - `session.py`: Defines the SQLAlchemy session.
  - `models/`: Contains SQLAlchemy models.
  - `dependencies.py`: Provides dependency overrides for FastAPI routes.
- `alembic/`: Contains Alembic migration scripts.
- `tests/`: Contains test cases using Pytest.

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd fastapi-sqlalchemy-alembic-pytest-sample
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**

   - Ensure your database server is running.
   - Update the database URL in `app/database/session.py` if necessary.

5. **Run migrations:**

   ```bash
   alembic upgrade head
   ```

6. **Run the application:**

   ```bash
   uvicorn app.main:app --reload
   ```

7. **Run tests:**

   ```bash
   pytest
   ```

## Troubleshooting

- If you encounter import errors, ensure all modules are correctly referenced using absolute imports.
- Verify that the database URL and credentials are correct in your environment.
- Ensure Alembic is correctly configured to point to your database.

## Additional Notes

- This setup assumes a PostgreSQL database, but you can modify the connection string for other databases.
- Alembic is used for managing database migrations. Ensure your `alembic.ini` is correctly configured.
- Pytest is used for testing. Ensure all test dependencies are installed and configured.

For more detailed information, refer to the official documentation of [FastAPI](https://fastapi.tiangolo.com/), [SQLAlchemy](https://www.sqlalchemy.org/), [Alembic](https://alembic.sqlalchemy.org/), and [Pytest](https://docs.pytest.org/).