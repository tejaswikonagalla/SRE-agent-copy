import sys
from pathlib import Path

# Add the base directory to the sys.path to ensure modules can be found
base_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(base_dir))

# Add the app directory to the sys.path to ensure app modules can be found
app_dir = base_dir / 'app'
sys.path.insert(0, str(app_dir))

# Remove the addition of the tests directory to sys.path
# as it is not necessary for resolving imports in the app module