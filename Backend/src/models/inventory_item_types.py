# Backend/src/models/inventory_item_types.py
# Description: Inventory item types model.

# Author: Valentin Haas, 2024

# System imports
from datetime import datetime
from typing import Optional

# Library imports
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_pascal
from sqlalchemy import Column, Integer, DateTime, String, Text, Boolean

# Project imports
from ._base import BaseTable


class InventoryItemTypesTable(BaseTable):
    """Definition of the InventoryItemTypes model for the database."""

    __tablename__ = "InventoryItemTypes"
    Id = Column(Integer, primary_key=True)
    """The unique identifier of the inventory item type."""

    Name = Column(String(64), nullable=False)
    """The name of the inventory item type."""

    Category = Column(Integer, nullable=True, foreign_key="ItemTypeCategories.Id")
    """The category of the inventory item type."""

    DefaultLocation = Column(Integer, nullable=False, foreign_key="RoomLocations.Id")
    """The default location of the inventory item type."""

    IsRentable = Column(Boolean, nullable=False, default=False)
    """Whether the inventory item type is rentable."""

    Description = Column(Text, nullable=True, default=None)
    """The description of the inventory item type."""

    ImagePath = Column(String, nullable=True, default=None)
    """The image path of the inventory item type."""

    AmountExisting = Column(Integer, nullable=True, default=None)
    """The amount of existing inventory items of this type."""

    AmountAvailable = Column(Integer, nullable=True, default=None)
    """The amount of available inventory items of this type."""

    PriceCt = Column(Integer, nullable=True, default=None)
    """The price of the inventory item type in cents."""

    ReplacementCostCt = Column(Integer, nullable=True, default=None)
    """The replacement cost of the inventory item type in cents."""

    Specifications = Column(Text, nullable=True, default=None)
    """The specifications of the inventory item type."""

    Comment = Column(Text, nullable=True, default=None)
    """A comment on the inventory item type."""

    CreationDate = Column(DateTime, nullable=False, default=datetime.now())
    """The creation date of the inventory item type."""

    LastChange = Column(DateTime, nullable=False, default=datetime.now())
    """The last change of the inventory item type."""

    def to_pydantic(self):
        return super().to_pydantic(self, InventoryItemType)


class InventoryItemType(BaseModel):
    """Definition of the InventoryItemTypes model for the API."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    id: int
    """The unique identifier of the inventory item type."""

    name: str
    """The name of the inventory item type."""

    category: int
    """The category of the inventory item type."""

    default_location: int
    """The default location of the inventory item type."""

    is_rentable: bool
    """Whether the inventory item type is rentable."""

    description: Optional[str] = None
    """The description of the inventory item type."""

    image_path: Optional[str] = None
    """The image path of the inventory item type."""

    amount_existing: Optional[int] = None
    """The amount of existing inventory items of this type."""

    amount_available: Optional[int] = None
    """The amount of available inventory items of this type."""

    price_ct: Optional[int] = None
    """The price of the inventory item type in cents."""

    replacement_cost_ct: Optional[int] = None
    """The replacement cost of the inventory item type in cents."""

    specifications: Optional[str] = None
    """The specifications of the inventory item type."""

    comment: Optional[str] = None
    """A comment on the inventory item type."""
