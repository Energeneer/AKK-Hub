# Backend/src/models/time_frames.py
# Definition of the TimeFrame model

# Author: Valentin Haas, 2024

# System imports
from datetime import datetime
from typing import Optional

# Library imports
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_pascal
from sqlalchemy import Column, Integer, DateTime

# Project imports
from ._base import BaseTable


class TimeFramesTable(BaseTable):
    """Model to track the time frames."""

    __tablename__ = "TimeFrames"
    Id = Column(Integer, primary_key=True)
    """The unique identifier of the time frame."""

    StartTime = Column(DateTime, nullable=False)
    """The start time of the time frame."""

    EndTime = Column(DateTime, nullable=False)
    """The end time of the time frame."""

    TimeSeries = Column(
        Integer, nullable=True, default=None, foreign_key="TimeSeries.Id"
    )
    """The unique identifier of the time series."""

    CreationDate = Column(DateTime, nullable=False, default=datetime.now())
    """The creation date of the time frame."""

    LastChange = Column(DateTime, nullable=False, default=datetime.now())
    """The last change date of the time frame."""

    def to_pydantic(self):
        return super().to_pydantic(self, TimeFrame)


class TimeFrame(BaseModel):
    """Definition of the TimeFrame model for the API."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    id: int
    """The unique identifier of the time frame."""

    start_time: datetime
    """The start time of the time frame."""

    end_time: datetime
    """The end time of the time frame."""

    time_series: Optional[int] = None
    """The unique identifier of the time series."""

    creation_date: Optional[datetime] = datetime.now()
    """The creation date of the time frame."""

    last_change: Optional[datetime] = datetime.now()
    """The last change date of the time frame."""
