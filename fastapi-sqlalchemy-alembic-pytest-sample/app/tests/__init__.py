import sys
from pathlib import Path

# Add the base directory to the sys.path to ensure modules can be found
base_dir = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(base_dir))

# Add the app directory to the sys.path to ensure app modules can be found
app_dir = base_dir / 'app'
sys.path.insert(0, str(app_dir))

# Add the tests directory to the sys.path to ensure test modules can be found
tests_dir = base_dir / 'app' / 'tests'
sys.path.insert(0, str(tests_dir))