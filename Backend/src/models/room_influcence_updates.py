# Backend/src/models/room_influcence_updates.py
# Definition of the RoomInflucenceUpdate model, tracking updates to room_influcences

# Author: Valentin Haas, 2024

# System imports
from typing import Optional
from datetime import datetime

# Library imports
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_pascal
from sqlalchemy import Column, DateTime, Enum, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

# Project imports
from .updates import UpdateType

# Constants
BASE = declarative_base()


class RoomInflucenceUpdatesTable(BASE):
    """Model to track the updates of room_influcences."""

    __tablename__ = "RoomInflucenceUpdates"
    Id = Column(Integer, primary_key=True)
    """The unique identifier of the room_influcence update."""

    RoomInflucence = Column(Integer, nullable=False)
    """The room_influcence affected by the update."""

    Time = Column(DateTime, nullable=False)
    """The time of the update."""

    Type = Column(Enum(UpdateType), nullable=False)
    """The type of the update."""

    Title = Column(String, nullable=False)
    """The title of the update."""

    UpdatedBy = Column(Integer, nullable=False, foreign_key="Users.Id")
    """The user who updated the room_influcence."""

    Text = Column(Text, nullable=True, default=None)
    """The text of the update."""


class RoomInflucenceUpdate(BaseModel):
    """Model to track the updates of room_influcences."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    id: int
    """The unique identifier of the room_influcence update."""

    room_influcence: int
    """The room_influcence affected by the update."""

    time: datetime
    """The time of the update."""

    type: UpdateType
    """The type of the update."""

    title: str
    """The title of the update."""

    updated_by: int
    """The user reference who updated the room_influcence."""

    text: Optional[str] = None
    """The text of the update."""
