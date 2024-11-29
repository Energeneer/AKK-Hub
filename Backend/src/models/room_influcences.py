# Backend/src/models/room_influcences.py
# Description: Room influences model for storing how room occupation affects other rooms.

# Author: Valentin Haas, 2024

# System imports
from datetime import datetime
from typing import Optional

# Library imports
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_pascal
from sqlalchemy import Boolean, Column, DateTime, Integer

# Project imports
from ._base import BaseTable


class RoomInfluencesTable(BaseTable):
    """Definition of the RoomInfluences model for the database."""

    __tablename__ = "RoomInfluences"
    Id = Column(Integer, primary_key=True)
    """The unique identifier of the room influence."""

    OccupiedRoom = Column(Integer, nullable=False, foreign_key="Rooms.Id")
    """The room that is occupied."""

    AffectedRoom = Column(Integer, nullable=False, foreign_key="Rooms.Id")
    """The room that is affected by the occupation."""

    AffectsAccess = Column(Boolean, nullable=False, default=False)
    """Whether the occupation affects access to the room."""

    AffectsSound = Column(Boolean, nullable=False, default=False)
    """Whether the occupation affects sound in the room."""

    AffectsSmell = Column(Boolean, nullable=False, default=False)
    """Whether the occupation affects smell in the room."""

    AffectsOccupation = Column(Boolean, nullable=False, default=False)
    """Whether the occupation affects occupation of the room."""

    CreationDate = Column(DateTime, nullable=False, default=datetime.now())
    """The creation date of the room influence entry."""

    LastChange = Column(DateTime, nullable=False, default=datetime.now())
    """The last change of the room influence entry."""

    def to_pydantic(self):
        return super().to_pydantic(self, RoomInfluence)


class RoomInfluence(BaseModel):
    """Definition of the RoomInfluences model for the API."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    id: int
    """The unique identifier of the room influence."""

    occupied_room: int
    """The room reference that is occupied."""

    affected_room: int
    """The room reference that is affected by the occupation."""

    affects_access: Optional[bool] = False
    """Whether the occupation affects access to the room."""

    affects_sound: Optional[bool] = False
    """Whether the occupation affects sound in the room."""

    affects_smell: Optional[bool] = False
    """Whether the occupation affects smell in the room."""

    affects_occupation: Optional[bool] = False
    """Whether the occupation affects occupation of the room."""

    creation_date: Optional[datetime] = datetime.now()
    """The creation date of the room influence entry."""

    last_change: Optional[datetime] = datetime.now()
    """The last change of the room influence entry."""
