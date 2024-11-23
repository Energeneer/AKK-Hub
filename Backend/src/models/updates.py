# Backend/src/models/updates.py
# Definitions for update tracking in the database

# Author: Valentin Haas, 2024

# System imports
from enum import Enum


class UpdateType(Enum):
    """Enumeration of the different types of updates."""

    OTHER = 0
    """An update of unknown type."""

    VAL_ADDITION = 11
    """An addition of a new value"""

    VAL_REMOVAL = 12
    """A removal of a value."""

    VAL_CHANGE = 13
    """A change of a value."""

    REF_ADDITION = 21
    """An addition of a reference."""

    REF_REMOVAL = 22
    """A removal of a reference."""

    REF_CHANGE = 23
    """A change of a reference."""
