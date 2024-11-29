# Backend/src/models/inventory_item_type_locations.py
# Description: Definition of the InventoryItemTypeLocation model, tracking the locations of inventory items

# Author: Valentin Haas, 2024

# Library imports
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_pascal
from sqlalchemy import Column, Integer

# Project imports
from ._base import BaseTable


class InventoryItemTypeLocationsTable(BaseTable):
    """Model to track the locations of inventory items."""

    __tablename__ = "InventoryItemTypeLocations"
    Id = Column(Integer, primary_key=True)
    """The unique identifier of the inventory item type location."""

    InventoryItemType = Column(
        Integer, nullable=False, foreign_key="InventoryItemTypes.Id"
    )
    """The key of the inventory item type."""

    Location = Column(Integer, nullable=False, foreign_key="RoomLocations.Id")
    """The key of the location."""

    Count = Column(Integer, nullable=False)
    """The count of the inventory item type at the location."""

    def to_pydantic(self):
        return super().to_pydantic(self, InventoryItemTypeLocation)


class InventoryItemTypeLocation(BaseModel):
    """Model to track the locations of inventory items."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    id: int
    """The unique identifier of the inventory item type location."""

    inventory_item_type: int
    """The inventory item type affected by the update."""

    location: int
    """The location of the inventory item type."""

    count: int
    """The count of the inventory item type at the location."""
