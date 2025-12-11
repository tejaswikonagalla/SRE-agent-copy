# Marks the app directory as a Python package.
# Ensure the package is recognized by adding an empty __init__.py file.

import sys
import os

# Add the parent directory to the system path to ensure proper module resolution
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Ensure the app directory is also in the system path for module resolution
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Import the necessary modules to ensure they are recognized during migrations
import app.models  # Assuming models.py exists in the app directory
import app.database  # Assuming database.py exists in the app directory