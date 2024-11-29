# Backend/src/models/item_reservations.py
# Definition of the ItemReservation model, tracking reservations of items (in events).

# Author: Valentin Haas, 2024

# System imports
from datetime import datetime
import enum
from typing import Optional

# Library imports
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_pascal
from sqlalchemy import Column, DateTime, Enum, Integer

# Project imports
from ._base import BaseTable


class ItemReservationStatus(enum.Enum):
    """Enum to define the status of an item reservation."""

    OPEN = 0
    """The reservation is open."""

    HANDED_OUT = 1
    """The item has been handed out."""

    RETURNED = 2
    """The item has been returned."""

    CANCELLED = 3
    """The reservation has been cancelled."""


class ItemReservationUnits(enum.Enum):
    """Enum to define the units of an item reservation."""

    Pieces = 0
    """The reservation is in pieces."""

    Boxes = 1
    """The reservation is in boxes."""

    Pallets = 2
    """The reservation is in pallets."""

    Kg = 3
    """The reservation is in kilograms."""

    Liters = 4
    """The reservation is in liters."""


class ItemReservationsTable(BaseTable):
    """Model to track reservations of items (in events)."""

    __tablename__ = "ItemReservations"

    Id = Column(Integer, primary_key=True)
    """The unique identifier of the item reservation."""

    TimeFrame = Column(Integer, nullable=False, foreign_key="TimeFrames.Id")
    """The time frame of the reservation."""

    ItemType = Column(Integer, nullable=False, foreign_key="InventoryItemTypes.Id")
    """The type of the item to reserve."""

    Unit = Column(Enum(ItemReservationUnits), nullable=False)
    """The unit of the reservation."""

    AmountHandedOut = Column(Integer, nullable=False)
    """The amount of the item that has been handed out."""

    HandedOutBy = Column(Integer, nullable=True, foreign_key="Users.Id")
    """The user who handed out the item."""

    AmountReturned = Column(Integer, nullable=True, default=0)
    """The amount of the item that has been returned."""

    ReturnAcceptedBy = Column(Integer, nullable=True, foreign_key="Users.Id")
    """The user who accepted the return of the item."""

    CreatedBy = Column(Integer, nullable=False, foreign_key="Users.Id")
    """The user who created the reservation."""

    Status = Column(Enum(ItemReservationStatus), nullable=False)
    """The status of the reservation."""

    CreationDate = Column(DateTime, nullable=False, default=datetime.now())
    """The creation date of the reservation."""

    LastChange = Column(DateTime, nullable=False, default=datetime.now())
    """The last change date of the reservation."""


class ItemReservation(BaseModel):
    """Definition of the ItemReservation model."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    id: int
    """The unique identifier of the item reservation."""

    time_frame: int
    """The time frame of the reservation."""

    item_type: int
    """The type of the item to reserve."""

    unit: int
    """The unit of the reservation."""

    amount_handed_out: Optional[int] = None
    """The amount of the item that has been handed out."""

    handed_out_by: Optional[int] = None
    """The user who handed out the item."""

    amount_returned: Optional[int] = None
    """The amount of the item that has been returned."""

    return_accepted_by: Optional[int] = None
    """The user who accepted the return of the item."""

    created_by: int
    """The user who created the reservation."""

    status: int
    """The status of the reservation."""

    creation_date: Optional[datetime] = datetime.now()
    """The creation date of the reservation."""

    last_change: Optional[datetime] = datetime.now()
    """The last change date of the reservation."""
