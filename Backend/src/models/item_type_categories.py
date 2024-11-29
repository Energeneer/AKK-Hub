# Backend/src/models/item_type_categories.py
# Definition of the ItemTypeCategory model, tracking the categories of inventory item types

# Author: Valentin Haas, 2024

# System imports
from datetime import datetime
from typing import Optional

# Library imports
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_pascal
from sqlalchemy import Column, DateTime, Integer, String, Text

# Project imports
from ._base import BaseTable


class ItemTypeCategoriesTable(BaseTable):
    """Model to track the categories of inventory item types."""

    __tablename__ = "ItemTypeCategories"
    Id = Column(Integer, primary_key=True)
    """The unique identifier of the item type category."""

    Name = Column(String, nullable=False)
    """The name of the item type category."""

    Description = Column(Text, nullable=True, default=None)
    """The description of the item type category."""

    CreationDate = Column(DateTime, nullable=False)
    """The creation date of the item type category."""

    LastChange = Column(DateTime, nullable=False)
    """The last change date of the item type category."""


class ItemTypeCategory(BaseModel):
    """Model to track the categories of inventory item types."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    id: int
    """The unique identifier of the item type category."""

    name: str
    """The name of the item type category."""

    description: Optional[str]
    """The description of the item type category."""

    creation_date: datetime
    """The creation date of the item type category."""

    last_change: datetime
    """The last change date of the item type category."""
