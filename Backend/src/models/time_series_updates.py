# Backend/src/models/time_series_updates.py
# Definition of the TimeSeriesUpdate model, tracking updates to time_seriess

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


class TimeSeriesUpdatesTable(BaseTable):
    """Model to track the updates of time_seriess."""

    __tablename__ = "TimeSeriesUpdates"
    Id = Column(Integer, primary_key=True)
    """The unique identifier of the time_series update."""

    TimeSeries = Column(Integer, nullable=False)
    """The key affected by the update."""

    Time = Column(DateTime, nullable=False)
    """The time of the update."""

    Type = Column(Enum(UpdateType), nullable=False)
    """The type of the update."""

    Title = Column(String, nullable=False)
    """The title of the update."""

    UpdatedBy = Column(Integer, nullable=False, foreign_key="Users.Id")
    """The user who updated the time_series."""

    Text = Column(Text, nullable=True, default=None)
    """The text of the update."""


class TimeSeriesUpdate(BaseModel):
    """Model to track the updates of time_seriess."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    id: int
    """The unique identifier of the time_series update."""

    time_series: int
    """The time_series affected by the update."""

    time: datetime
    """The time of the update."""

    type: UpdateType
    """The type of the update."""

    title: str
    """The title of the update."""

    updated_by: int
    """The user reference who updated the time_series."""

    text: Optional[str] = None
    """The text of the update."""
