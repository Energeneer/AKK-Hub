# Backend/src/models/room_reservations.py
# Definition of the RoomReservation model

# Author: Valentin Haas, 2024

# System imports
from datetime import datetime
from typing import Optional
import enum

# Library imports
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_pascal
from sqlalchemy import Column, Enum, DateTime, Integer, Text

# Project imports
from ._base import BaseTable


class RoomReservationStatus(enum.Enum):
    """Enum to track the status of the room reservation."""

    PENDING = 0
    """The room reservation is pending."""

    ACCEPTED = 1
    """The room reservation is accepted."""

    DECLINED = 2
    """The room reservation is declined."""


class RoomReservationsTable(BaseTable):
    """Model to track the room reservations."""

    __tablename__ = "RoomReservations"
    Id = Column(Integer, primary_key=True)
    """The unique identifier of the room reservation."""

    TimeFrame = Column(Integer, nullable=False, foreign_key="TimeFrames.Id")
    """The time frame of the room reservation."""

    Room = Column(Integer, nullable=False, foreign_key="RoomLocations.Id")
    """The room of the room reservation."""

    CreatedBy = Column(Integer, nullable=False, foreign_key="Users.Id")
    """The user who created the room reservation."""

    CreationDate = Column(DateTime, nullable=False, default=datetime.now())
    """The creation date of the room reservation."""

    Status = Column(Enum(RoomReservationStatus), nullable=False)
    """The status of the room reservation."""

    LastChange = Column(DateTime, nullable=False, default=datetime.now())
    """The last change date of the room reservation."""

    Changelog = Column(Text, nullable=True, default=None)
    """The changelog of the room reservation."""

    def to_pydantic(self):
        return super().to_pydantic(self, RoomReservation)


class RoomReservation(BaseModel):
    """Definition of the RoomReservation model for the API."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    id: int
    """The unique identifier of the room reservation."""

    time_frame: int
    """The time frame of the room reservation."""

    room: int
    """The room of the room reservation."""

    created_by: int
    """The user who created the room reservation."""

    creation_date: Optional[datetime] = datetime.now()
    """The creation date of the room reservation."""

    status: RoomReservationStatus
    """The status of the room reservation."""

    last_change: Optional[datetime] = datetime.now()
    """The last change date of the room reservation."""

    changelog: Optional[str] = None
    """The changelog of the room reservation."""
