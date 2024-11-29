# Backend/src/models/room_updates.py
# Definition of the RoomUpdate model, tracking updates to rooms

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


class RoomUpdatesTable(BaseTable):
    """Model to track the updates of rooms."""

    __tablename__ = "RoomUpdates"
    Id = Column(Integer, primary_key=True)
    """The unique identifier of the room update."""

    Room = Column(Integer, nullable=False)
    """The room affected by the update."""

    Time = Column(DateTime, nullable=False)
    """The time of the update."""

    Type = Column(Enum(UpdateType), nullable=False)
    """The type of the update."""

    Title = Column(String, nullable=False)
    """The title of the update."""

    UpdatedBy = Column(Integer, nullable=False, foreign_key="Users.Id")
    """The user who updated the room."""

    Text = Column(Text, nullable=True, default=None)
    """The text of the update."""

    def to_pydantic(self):
        return super().to_pydantic(self, RoomUpdate)


class RoomUpdate(BaseModel):
    """Model to track the updates of rooms."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    id: int
    """The unique identifier of the room update."""

    room: int
    """The room affected by the update."""

    time: datetime
    """The time of the update."""

    type: UpdateType
    """The type of the update."""

    title: str
    """The title of the update."""

    updated_by: int
    """The user reference who updated the room."""

    text: Optional[str] = None
    """The text of the update."""
