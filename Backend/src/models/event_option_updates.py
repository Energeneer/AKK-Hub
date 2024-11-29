# Backend/src/models/event_option_updates.py
# Definition of the EventOptionUpdate model, tracking updates to EventOptions

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


class EventOptionUpdatesTable(BASE):
    """Model to track the updates of EventOptions."""

    __tablename__ = "EventOptionUpdates"
    Id = Column(Integer, primary_key=True)
    """The unique identifier of the EventOption update."""

    EventOption = Column(Integer, nullable=False)
    """The EventOption affected by the update."""

    Time = Column(DateTime, nullable=False)
    """The time of the update."""

    Type = Column(Enum(UpdateType), nullable=False)
    """The type of the update."""

    Title = Column(String, nullable=False)
    """The title of the update."""

    UpdatedBy = Column(Integer, nullable=False, foreign_key="Users.Id")
    """The user who updated the EventOption."""

    Text = Column(Text, nullable=True, default=None)
    """The text of the update."""


class EventOptionUpdate(BaseModel):
    """Model to track the updates of EventOptions."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    id: int
    """The unique identifier of the EventOption update."""

    event_option: int
    """The EventOption affected by the update."""

    time: datetime
    """The time of the update."""

    type: UpdateType
    """The type of the update."""

    title: str
    """The title of the update."""

    updated_by: int
    """The user who updated the EventOption."""

    text: Optional[str]
    """The text of the update."""
