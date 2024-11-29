# Backend/src/models/item_tag_groups.py
# Description: Item tag groups model.

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


class ItemTagGroupsTable(BaseTable):
    """Model to track the item tag groups."""

    __tablename__ = "ItemTagGroups"
    Id = Column(Integer, primary_key=True)
    """The unique identifier of the item tag group."""

    Name = Column(String(64), nullable=False)
    """The name of the item tag group."""

    Description = Column(Text, nullable=True, default=None)
    """The description of the item tag group."""

    CreationDate = Column(DateTime, nullable=False)
    """The creation date of the item tag group."""

    LastChange = Column(DateTime, nullable=False)
    """The last change date of the item tag group."""


class ItemTagGroup(BaseModel):
    """Model to track the item tag groups."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    id: int
    """The unique identifier of the item tag group."""

    name: str
    """The name of the item tag group."""

    description: Optional[str]
    """The description of the item tag group."""

    creation_date: Optional[datetime] = datetime.now()
    """The creation date of the item tag group."""

    last_change: Optional[datetime] = datetime.now()
    """The last change date of the item tag group."""
