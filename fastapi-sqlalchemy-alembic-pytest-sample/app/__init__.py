# Marks the app directory as a Python package.
# Ensure the package is recognized by adding an empty __init__.py file.

import sys
import os

# Add the parent directory to the system path to ensure proper module resolution
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))