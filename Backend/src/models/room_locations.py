# Backend/src/models/room_locations.py
# Definition of locations within a room. May be recursive to allow for nested locations.

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


class RoomLocationsTable(BASE):
    """Definition of the RoomLocations model for the database."""

    __tablename__ = "RoomLocations"
    Id = Column(Integer, primary_key=True)
    """The unique identifier of the location."""

    Name = Column(String, nullable=False)
    """The name of the location."""

    Room = Column(Integer, nullable=False, foreign_key="Rooms.Id")
    """The room in which the location is located."""

    RoomLocation = Column(Integer, nullable=True, foreign_key="RoomLocations.Id")
    """The parent location of the location."""

    Description = Column(Text, nullable=True, default=None)
    """The description of the location."""

    ImagePath = Column(String, nullable=True, default=None)
    """The path to the image of the location."""

    CreationDate = Column(DateTime, nullable=False, default=datetime.now())
    """The creation date of the location."""

    LastChange = Column(DateTime, nullable=False, default=datetime.now())
    """The last change date of the location."""


class RoomLocations(BaseModel):
    """Definition of the RoomLocations model for the API."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    id: int
    """The unique identifier of the location."""

    name: str
    """The name of the location."""

    room: int
    """The room in which the location is located."""

    room_location: Optional[int] = None
    """The parent room location id of the location."""

    description: Optional[str] = None
    """The description of the location."""

    image_path: Optional[str] = None
    """The path to the image of the location."""

    creation_date: datetime
    """The creation date of the location."""

    last_change: datetime
    """The last change date of the location."""
