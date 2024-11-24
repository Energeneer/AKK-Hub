# Backend/src/models/key_ring_updates.py
# Definition of the KeyUpdate model, tracking updates to key_rings

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


class KeyUpdatesTable(BASE):
    """Model to track the updates of key_rings."""

    __tablename__ = "KeyUpdates"
    Id = Column(Integer, primary_key=True)
    """The unique identifier of the key_ring update."""

    Key = Column(Integer, nullable=False)
    """The key affected by the update."""

    Time = Column(DateTime, nullable=False)
    """The time of the update."""

    Type = Column(UpdateType, nullable=False)
    """The type of the update."""

    Title = Column(String, nullable=False)
    """The title of the update."""

    UpdatedBy = Column(Integer, nullable=False, foreign_key="Users.Id")
    """The key_ring who updated the key_ring."""

    Text = Column(Text, nullable=True, default=None)
    """The text of the update."""


class KeyUpdate(BaseModel):
    """Model to track the updates of key_rings."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    id: int
    """The unique identifier of the key_ring update."""

    key_ring: int
    """The key_ring affected by the update."""

    time: datetime
    """The time of the update."""

    type: UpdateType
    """The type of the update."""

    title: str
    """The title of the update."""

    updated_by: int
    """The person reference who updated the key_ring."""

    text: Optional[str] = None
    """The text of the update."""