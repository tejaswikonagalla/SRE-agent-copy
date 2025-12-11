from app.models.book import Book
from app.models.model_base import ModelBase

# Ensure that the book.py and model_base.py files exist in the same directory as this __init__.py file
# and contain at least a minimal definition of the Book class and ModelBase class respectively.

__all__ = ["Book", "ModelBase"]