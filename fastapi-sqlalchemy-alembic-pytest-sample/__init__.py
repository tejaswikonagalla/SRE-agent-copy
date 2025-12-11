# This file marks the project root as a Python package.

import sys
import os

# Add the project root to the Python path to ensure modules can be found
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Ensure the 'app' directory is also added to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'app')))