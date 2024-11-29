# Backend/src/models/room_location_updates.py
# Definition of the RoomLocationUpdate model, tracking updates to room_locations

# Author: Valentin Haas, 2024

# System imports
from datetime import datetime
from typing import Optional

# Library imports
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_pascal
from sqlalchemy import Column, DateTime, Enum, Integer, String, Text

# Project imports
from ._base import BaseTable
from .updates import UpdateType


class RoomLocationUpdatesTable(BaseTable):
    """Model to track the updates of room_locations."""

    __tablename__ = "RoomLocationUpdates"
    Id = Column(Integer, primary_key=True)
    """The unique identifier of the room_location update."""

    RoomLocation = Column(Integer, nullable=False)
    """The room_location affected by the update."""

    Time = Column(DateTime, nullable=False)
    """The time of the update."""

    Type = Column(Enum(UpdateType), nullable=False)
    """The type of the update."""

    Title = Column(String, nullable=False)
    """The title of the update."""

    UpdatedBy = Column(Integer, nullable=False, foreign_key="Users.Id")
    """The user who updated the room_location."""

    Text = Column(Text, nullable=True, default=None)
    """The text of the update."""


class RoomLocationUpdate(BaseModel):
    """Model to track the updates of room_locations."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    id: int
    """The unique identifier of the room_location update."""

    room_location: int
    """The room_location affected by the update."""

    time: datetime
    """The time of the update."""

    type: UpdateType
    """The type of the update."""

    title: str
    """The title of the update."""

    updated_by: int
    """The user reference who updated the room_location."""

    text: Optional[str] = None
    """The text of the update."""
