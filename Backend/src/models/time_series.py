# Backend/src/models/time_series.py
# Definition of the TimeSeries model

# Author: Valentin Haas, 2024

# System imports
from datetime import datetime
from typing import Optional

# Library imports
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_pascal
from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.ext.declarative import declarative_base

# Constants
BASE = declarative_base()


class TimeSeriesTable(BASE):
    """Model to track the time series."""

    __tablename__ = "TimeSeries"
    Id = Column(Integer, primary_key=True)
    """The unique identifier of the time series."""

    Rule = Column(String, nullable=False)
    """The rule of the time series."""

    CreationDate = Column(DateTime, nullable=False, default=datetime.now())
    """The creation date of the time series."""

    LastChange = Column(DateTime, nullable=False, default=datetime.now())
    """The last change date of the time series."""


class TimeSeries(BaseModel):
    """Definition of the TimeSeries model for the API."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    id: int
    """The unique identifier of the time series."""

    rule: str
    """The rule of the time series."""

    creation_date: Optional[datetime] = datetime.now()
    """The creation date of the time series."""

    last_change: Optional[datetime] = datetime.now()
    """The last change date of the time series."""
