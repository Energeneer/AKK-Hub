# Backend/src/models/address_updates.py
# Definition of the AddressUpdate model, tracking updates to Addresses

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


class AddressUpdatesTable(BaseTable):
    """Model to track the updates of Addresses."""

    __tablename__ = "AddressUpdates"
    Id = Column(Integer, primary_key=True)
    """The unique identifier of the Address update."""

    Address = Column(Integer, nullable=False)
    """The Address affected by the update."""

    Time = Column(DateTime, nullable=False)
    """The time of the update."""

    Type = Column(Enum(UpdateType), nullable=False)
    """The type of the update."""

    Title = Column(String, nullable=False)
    """The title of the update."""

    UpdatedBy = Column(Integer, nullable=False, foreign_key="Users.Id")
    """The user who updated the address."""

    Text = Column(Text, nullable=True, default=None)
    """The text of the update."""

    def to_pydantic(self):
        return super().to_pydantic(self, AddressUpdate)


class AddressUpdate(BaseModel):
    """Model to track the updates of Addresses."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    id: int
    """The unique identifier of the address update."""

    address: int
    """The address affected by the update."""

    time: datetime
    """The time of the update."""

    type: UpdateType
    """The type of the update."""

    title: str
    """The title of the update."""

    updated_by: int
    """The user reference who updated the Address."""

    text: Optional[str]
    """The text of the update."""
