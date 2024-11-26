# Backend/src/models/event_updates.py
# Definition of the EventUpdate model, tracking updates to Events

# Author: Valentin Haas, 2024

# System imports
from typing import Optional
from datetime import datetime

# Library imports
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_pascal
from sqlalchemy import Column, Integer, DateTime, String, Text
from sqlalchemy.ext.declarative import declarative_base

# Project imports
from updates import UpdateType

# Constants
BASE = declarative_base()


class EventUpdatesTable(BASE):
    """Model to track the updates of Events."""

    __tablename__ = "EventUpdates"
    Id = Column(Integer, primary_key=True)
    """The unique identifier of the Event update."""

    Event = Column(Integer, nullable=False)
    """The Event affected by the update."""

    Time = Column(DateTime, nullable=False)
    """The time of the update."""

    Type = Column(UpdateType, nullable=False)
    """The type of the update."""

    Title = Column(String, nullable=False)
    """The title of the update."""

    UpdatedBy = Column(Integer, nullable=False, foreign_key="Users.Id")
    """The user who updated the Event."""

    Text = Column(Text, nullable=True, default=None)
    """The text of the update."""


class EventUpdate(BaseModel):
    """Model to track the updates of Events."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    id: int
    """The unique identifier of the Event update."""

    event: int
    """The Event affected by the update."""

    time: datetime
    """The time of the update."""

    type: UpdateType
    """The type of the update."""

    title: str
    """The title of the update."""

    updated_by: int
    """The user who updated the Event."""

    text: Optional[str]
    """The text of the update."""
