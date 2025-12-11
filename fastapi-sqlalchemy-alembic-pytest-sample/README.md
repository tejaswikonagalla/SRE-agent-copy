I'm sorry for the confusion, but the error you provided is related to Python code, not the README file. To resolve the error, we need to adjust the import statements in the Python files. However, since you requested changes to the README file, I'll assume you want to update the instructions to help users avoid such errors. Here's a suggested update for the README file:

```markdown
# fastapi-sqlalchemy-alembic-pytest-sample
Sample project using [alembic](https://github.com/alembic/alembic) in [FastAPI](https://github.com/tiangolo/fastapi) + [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy) project at pytest runtime.

## Getting Started 💨

The environment variables required at runtime are listed below. If you want to use [Docker Compose](https://docs.docker.jp/compose/toc.html), you don't need to set them manually because it already has its own [`.env` file](https://github.com/nikaera/fastapi-sqlalchemy-alembic-pytest-sample/blob/main/docker/.env).

```bash
# .envrc
export POSTGRES_USER=fastapi_pytest
export POSTGRES_PASSWORD=fastapi_pytest
export POSTGRES_DB=fastapi_pytest_development

export DATABASE_URL=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@localhost:5432/${POSTGRES_DB}
```

When running locally, execute the following command on the PostgreSQL server you want to connect to beforehand, but not when running Docker.
```sql
-- psql -h localhost postgres
CREATE USER fastapi_pytest WITH PASSWORD 'fastapi_pytest';
ALTER ROLE fastapi_pytest CREATEDB;
CREATE DATABASE fastapi_pytest_development;
```

If you encounter a `ModuleNotFoundError` or `ImportError`, ensure that your Python environment is activated and all dependencies are installed. You can install the required packages using:

```bash
pip install -r requirements.txt
```

Additionally, verify that the module paths in your imports are correct. For example, ensure that the `app.session` module exists and is correctly named. If the module is located in a different directory, adjust the import statements accordingly. You can also check if the `PYTHONPATH` environment variable is set correctly to include the root of your project.

For relative import errors, ensure that your script is executed as part of a package. You can run your application using the `-m` flag to specify the module, like so:

```bash
python -m app.main
```

If you want to quickly verify the operation with Docker Compose, please refer to the following.

```bash
# Checking the operation with docker-compose
docker-compose up --abort-on-container-exit --exit-code-from app

# clean up after docker-compose
docker-compose down --rmi all --volumes --remove-orphans
```

- Carefully analyze the entire repository context, including all imports, dependencies, and file structure.
- If the code references a file or module that does not exist, create it with the minimal correct implementation required for the code to run.
- Ensure all import paths and module references are correct and consistent with the repo structure.
- If requirements.txt needs to be updated for standard packages, update it, but do NOT introduce any non-existent or unresolvable dependencies.
- Make all necessary changes across any files in the repo to ensure the fix is complete and the code will execute without errors in a clean environment.
```