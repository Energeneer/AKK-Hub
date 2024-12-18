# Backend/src/models/item_tags_to_inventory_item_types.py
# Many-to-many relationship between item tags and inventory item types.

# Author: Valentin Haas, 2024

# Library imports
from sqlalchemy import Column, Integer
from ._base import BaseTable


class ItemTagsToInventoryItemTypesTable(BaseTable):
    """Model to track the many-to-many relationship between item tags and inventory item types."""

    __tablename__ = "ItemTagsToInventoryItemTypes"
    ItemTag = Column(Integer, primary_key=True, foreign_key="ItemTags.Id")
    """The item tag of the relationship."""

    InventoryItemType = Column(
        Integer, primary_key=True, foreign_key="InventoryItemTypes.Id"
    )
    """The inventory item type of the relationship."""
