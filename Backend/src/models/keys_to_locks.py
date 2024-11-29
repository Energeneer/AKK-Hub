# Backend/src/models/keys_to_locks.py
# Many to Many relationship between keys and locks, i.e. which keys can open which locks.
# Direct association, should we use an electronik keycard system with individual associations.

# Author: Valentin Haas, 2024

# Library imports
from sqlalchemy import Column, Integer

# Project imports
from ._base import BaseTable


class KeysToLocksTable(BaseTable):
    """Model to track the relationship between keys and locks."""

    __tablename__ = "KeysToLocks"

    Key = Column(Integer, primary_key=True, foreign_key="Keys.Id")
    """The key in the relationship."""

    Lock = Column(Integer, primary_key=True, foreign_key="Locks.Id")
    """The lock in the relationship."""
