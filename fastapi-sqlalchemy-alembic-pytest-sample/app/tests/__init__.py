import sys
from pathlib import Path

# Add the app directory to the sys.path to ensure modules can be found
app_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(app_dir))