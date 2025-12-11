import sys
from pathlib import Path

# Add the base directory to the sys.path to ensure modules can be found
base_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(base_dir))

# Add the app directory to the sys.path to ensure app modules can be found
app_dir = base_dir / 'app'
sys.path.insert(0, str(app_dir))

# Ensure the tests directory is not in sys.path to avoid import conflicts
tests_dir = base_dir / 'tests'
if str(tests_dir) in sys.path:
    sys.path.remove(str(tests_dir))

# Ensure the database URL or any other environment variables are set correctly
import os

# Example: Set a default database URL if not already set
os.environ.setdefault('DATABASE_URL', 'sqlite:///test.db')