# Backend/src/models/address_updates.py
# Definition of the AddressUpdate model, tracking updates to Addresses

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


class AddressUpdatesTable(BASE):
    """Model to track the updates of Addresses."""

    __tablename__ = "AddressUpdates"
    Id = Column(Integer, primary_key=True)
    """The unique identifier of the Address update."""

    Address = Column(Integer, nullable=False)
    """The Address affected by the update."""

    Time = Column(DateTime, nullable=False)
    """The time of the update."""

    Type = Column(UpdateType, nullable=False)
    """The type of the update."""

    Title = Column(String, nullable=False)
    """The title of the update."""

    UpdatedBy = Column(Integer, nullable=False, foreign_key="Users.Id")
    """The user who updated the Address."""

    Text = Column(Text, nullable=True, default=None)
    """The text of the update."""


class AddressUpdate(BaseModel):
    """Model to track the updates of Addresses."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    id: int
    """The unique identifier of the Address update."""

    address: int
    """The Address affected by the update."""

    time: datetime
    """The time of the update."""

    type: UpdateType
    """The type of the update."""

    title: str
    """The title of the update."""

    updated_by: int
    """The user who updated the Address."""

    text: Optional[str]
    """The text of the update."""
