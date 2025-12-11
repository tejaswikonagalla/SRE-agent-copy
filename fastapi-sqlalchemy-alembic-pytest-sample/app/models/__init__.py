from .book import Book

# Ensure that the book.py file exists in the same directory as this __init__.py file
# and contains at least a minimal definition of the Book class.

# Import all models here to ensure they are registered with SQLAlchemy's metadata
# This is necessary for Alembic to detect changes in the models for migrations.
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Example of registering the Book model with the Base
Book.__table__.metadata = Base.metadata