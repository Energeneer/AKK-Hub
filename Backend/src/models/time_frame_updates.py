# Backend/src/models/time_frame_updates.py
# Definition of the TimeFrameUpdate model, tracking updates to time_frames

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


class TimeFrameUpdatesTable(BaseTable):
    """Model to track the updates of time_frames."""

    __tablename__ = "TimeFrameUpdates"
    Id = Column(Integer, primary_key=True)
    """The unique identifier of the time_frame update."""

    TimeFrame = Column(Integer, nullable=False)
    """The key affected by the update."""

    Time = Column(DateTime, nullable=False)
    """The time of the update."""

    Type = Column(Enum(UpdateType), nullable=False)
    """The type of the update."""

    Title = Column(String, nullable=False)
    """The title of the update."""

    UpdatedBy = Column(Integer, nullable=False, foreign_key="Users.Id")
    """The user who updated the time_frame."""

    Text = Column(Text, nullable=True, default=None)
    """The text of the update."""

    def to_pydantic(self):
        return super().to_pydantic(self, TimeFrameUpdate)


class TimeFrameUpdate(BaseModel):
    """Model to track the updates of time_frames."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    id: int
    """The unique identifier of the time_frame update."""

    time_frame: int
    """The time_frame affected by the update."""

    time: datetime
    """The time of the update."""

    type: UpdateType
    """The type of the update."""

    title: str
    """The title of the update."""

    updated_by: int
    """The user reference who updated the time_frame."""

    text: Optional[str] = None
    """The text of the update."""
