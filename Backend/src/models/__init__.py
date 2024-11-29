# Backend/src/models/__init__.py
# Imports all models into the package namespace

# Author: Valentin Haas, 2024

# System imports
import os
import importlib


# Constants
MODEL_FILES = [
    py_file
    for py_file in os.listdir(os.path.dirname(__file__))
    if py_file.endswith(".py") and py_file != "__init__.py"
]
MODULES = [py_file[:-3] for py_file in MODEL_FILES]


# Dynamically import all models
for module in MODULES:
    importlib.import_module(f".{module}", package=__name__)
