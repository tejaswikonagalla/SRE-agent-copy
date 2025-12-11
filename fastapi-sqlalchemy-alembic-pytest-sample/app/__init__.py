# Marks the app directory as a Python package.
# Ensure the package is recognized by adding an empty __init__.py file.

import sys
import os

# Add the grandparent directory to the system path to ensure proper module resolution
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Import the necessary modules for database migration
from alembic import command
from alembic.config import Config

def run_migrations():
    # Set up the Alembic configuration
    alembic_cfg = Config(os.path.join(os.path.dirname(__file__), 'alembic.ini'))
    # Run the migrations
    command.upgrade(alembic_cfg, 'head')

# Execute migrations when the module is run as a script
if __name__ == "__main__":
    run_migrations()