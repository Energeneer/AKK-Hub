# Backend/src/models/item_reservation_updates.py
# Definition of the ItemReservationUpdate model, tracking updates to item_reservations

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


class ItemReservationUpdatesTable(BaseTable):
    """Model to track the updates of inventory item types."""

    __tablename__ = "ItemReservationUpdates"
    Id = Column(Integer, primary_key=True)
    """The unique identifier of the inventory item type update."""

    ItemReservation = Column(Integer, nullable=False)
    """The key affected by the update."""

    Time = Column(DateTime, nullable=False)
    """The time of the update."""

    Type = Column(Enum(UpdateType), nullable=False)
    """The type of the update."""

    Title = Column(String, nullable=False)
    """The title of the update."""

    UpdatedBy = Column(Integer, nullable=False, foreign_key="Users.Id")
    """The user who updated the inventory item type."""

    Text = Column(Text, nullable=True, default=None)
    """The text of the update."""

    def to_pydantic(self):
        return super().to_pydantic(self, ItemReservationUpdate)


class ItemReservationUpdate(BaseModel):
    """Model to track the updates of inventory item types."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    id: int
    """The unique identifier of the inventory item type update."""

    item_reservation_type: int
    """The inventory item type affected by the update."""

    time: datetime
    """The time of the update."""

    type: UpdateType
    """The type of the update."""

    title: str
    """The title of the update."""

    updated_by: int
    """The person reference who updated the inventory item type."""

    text: Optional[str] = None
    """The text of the update."""
