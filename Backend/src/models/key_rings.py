# Backend/src/models/key_rings.py
# Definition of the KeyRing model

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


class KeyRingsTable(BASE):
    """Definition of the KeyRing model for the database."""

    __tablename__ = "KeyRings"
    Id = Column(Integer, primary_key=True)
    """The unique identifier of the key ring."""

    Label = Column(String, nullable=False)
    """The label of the key ring."""

    Description = Column(Text, nullable=True, default=None)
    """The description of the key ring."""

    ImagePath = Column(String, nullable=True, default=None)
    """The path to the image of the key ring."""

    DefaultLocation = Column(Integer, nullable=False, foreign_key="RoomLocations.Id")
    """The default location of the key ring."""

    CurrentLocation = Column(Integer, nullable=False, foreign_key="RoomLocations.Id")
    """The current location of the key ring."""

    CreationDate = Column(DateTime, nullable=False, default=datetime.now())
    """The creation date of the key ring."""

    LastChange = Column(DateTime, nullable=False, default=datetime.now())
    """The last change date of the key ring."""


class KeyRing(BaseModel):
    """Definition of the KeyRing model for the API."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    id: int
    """The unique identifier of the key ring."""

    label: str
    """The label of the key ring."""

    description: Optional[str] = None
    """The description of the key ring."""

    image_path: Optional[str] = None
    """The path to the image of the key ring."""

    default_location: int
    """The default location of the key ring."""

    current_location: int
    """The current location of the key ring."""

    creation_date: Optional[datetime] = datetime.now()
    """The creation date of the key ring."""

    last_change: Optional[datetime] = datetime.now()
    """The last change date of the key ring."""
