# Marks the app directory as a Python package.
# Ensure the package is recognized by adding an empty __init__.py file.

import sys
import os

# Add the app directory to the system path to ensure proper module resolution
sys.path.append(os.path.dirname(os.path.abspath(__file__)))