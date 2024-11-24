# Backend/src/models/locks.py
# Definition of the Lock model

# Author: Valentin Haas, 2024

# System imports
from datetime import datetime
from typing import Optional

# Library imports
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_pascal
from sqlalchemy import Column, Integer, Date, DateTime, String, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base

# Constants
BASE = declarative_base()


class LocksTable(BASE):
    """Definition of the Lock model for the database."""

    __tablename__ = "Locks"
    Id = Column(Integer, primary_key=True)
    """The unique identifier of the lock."""

    Type = Column(Integer, nullable=False, foreign_key="LockTypes.Id")
    """The type of the lock."""

    Number = Column(Integer, nullable=False, unique=True)
    """The number of the lock."""

    DefaultLocation = Column(Integer, nullable=False, foreign_key="RoomLocations.Id")
    """The default location of the lock."""

    CurrentLocation = Column(Integer, nullable=False, foreign_key="RoomLocations.Id")
    """The current location of the lock."""

    CreationDate = Column(DateTime, nullable=False, default=datetime.now())
    """The creation date of the lock."""

    LastChange = Column(DateTime, nullable=False, default=datetime.now())
    """The last change date of the lock."""


class Lock(BaseModel):
    """Definition of the Lock model for the API."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    id: int
    """The unique identifier of the lock."""

    type: int
    """The type of the lock."""

    number: int
    """The number of the lock."""

    default_location: int
    """The default location of the lock."""

    current_location: int
    """The current location of the lock."""

    creation_date: Optional[datetime] = datetime.now()
    """The creation date of the lock."""

    last_change: Optional[datetime] = datetime.now()
    """The last change date of the lock."""
