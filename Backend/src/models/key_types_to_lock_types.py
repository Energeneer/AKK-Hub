# Backend/src/models/key_types_to_lock_types.py
# Many to Many relationship between key types and lock types, i.e. which key types can open which lock types

# Author: Valentin Haas, 2024

# Library imports
from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

# Constants
BASE = declarative_base()


class KeyTypesToLockTypesTable(BASE):
    """Model to track the relationship between key types and lock types."""

    __tablename__ = "KeyTypesToLockTypes"

    KeyType = Column(Integer, primary_key=True, foreign_key="KeyTypes.Id")
    """The key type in the relationship."""

    LockType = Column(Integer, primary_key=True, foreign_key="LockTypes.Id")
    """The lock type in the relationship."""
