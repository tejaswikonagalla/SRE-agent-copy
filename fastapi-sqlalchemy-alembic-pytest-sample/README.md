# FastAPI SQLAlchemy Alembic Pytest Sample

This repository is a sample project demonstrating how to use FastAPI with SQLAlchemy, Alembic, and Pytest.

## Project Structure

- `app/`: Contains the main application code.
  - `main.py`: The entry point for the FastAPI application.
  - `database/`: Contains database-related modules.
    - `session.py`: Defines the SQLAlchemy session.
  - `models/`: Contains SQLAlchemy models.
  - `routers/`: Contains API route definitions.
  - `dependencies.py`: Contains dependency functions for the application.
- `alembic/`: Contains Alembic migration scripts.
- `tests/`: Contains test cases for the application.

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/fastapi-sqlalchemy-alembic-pytest-sample.git
   cd fastapi-sqlalchemy-alembic-pytest-sample
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**

   - Update the database URL in `app/database/session.py`.
   - Run Alembic migrations to set up the database schema:

     ```bash
     alembic upgrade head
     ```

5. **Run the application:**

   ```bash
   uvicorn app.main:app --reload
   ```

6. **Run tests:**

   ```bash
   pytest
   ```

## Notes

- Ensure that all import statements in the codebase use absolute imports based on the project structure.
- If you encounter any issues with migrations, check the Alembic configuration and migration scripts.