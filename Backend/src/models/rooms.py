# Backend/src/models/rooms.py
# Definition of the Room model

# Author: Valentin Haas, 2024

# System imports
from datetime import datetime
from typing import Optional

# Library imports
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_pascal
from sqlalchemy import Boolean, Column, DateTime, Integer, Numeric, String, Text

# Project imports
from ._base import BaseTable


class RoomsTable(BaseTable):
    """Definition of the Room model for the database."""

    __tablename__ = "Rooms"
    Id = Column(Integer, primary_key=True)
    """The unique identifier of the room."""

    Building = Column(Integer, nullable=False)
    """The building reference of the room."""

    Name = Column(String, nullable=False)
    """The name of the room."""

    Description = Column(Text, nullable=True, default=None)
    """The description of the room."""

    RoomNumber = Column(String, nullable=True, default=None)
    """The room number of the room."""

    CanBeBooked = Column(Boolean, nullable=False, default=False)
    """Whether the room can be booked."""

    SizeSqm = Column(Numeric, nullable=True, default=None)
    """The size of the room in square meters."""

    CapacityPpl = Column(Integer, nullable=True, default=None)
    """The capacity of the room in people."""

    LastChange = Column(DateTime, nullable=False, default=datetime.now())
    """The last change of the room entry."""


class Rooms(BaseModel):
    """Definition of the Room model for the API."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    id: int
    """The unique identifier of the room."""

    building: int
    """The building reference of the room."""

    name: str
    """The name of the room."""

    description: Optional[str]
    """The description of the room."""

    room_number: Optional[str]
    """The room number of the room."""

    can_be_booked: Optional[bool] = False
    """Whether the room can be booked."""

    size_sqm: Optional[float]
    """The size of the room in square meters."""

    capacity_ppl: Optional[int]
    """The capacity of the room in people."""

    last_change: datetime
    """The last change of the room entry."""
