import os
import sys
from sqlalchemy.orm import declarative_base

# Ensure the app directory is in the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
app_dir = os.path.join(current_dir, '..')
sys.path.insert(0, app_dir)

ModelBase = declarative_base()