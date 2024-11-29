# Backend/src/models/item_tags.py
# Definition of the ItemTag model, tracking the tags of inventory items

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


class ItemTagsTable(BaseTable):
    """Model to track the tags of inventory items."""

    __tablename__ = "ItemTags"
    Id = Column(Integer, primary_key=True)
    """The unique identifier of the item tag."""

    Name = Column(String, nullable=False)
    """The name of the tag."""

    TagGroup = Column(
        Integer, nullable=True, foreign_key="ItemTagGroups.Id", default=None
    )
    """The tag group the tag is associated with."""

    Description = Column(Text, nullable=True, default=None)
    """The description of the tag."""

    CreationDate = Column(DateTime, nullable=False)
    """The creation date of the tag."""

    LastChange = Column(DateTime, nullable=False)
    """The last change date of the tag."""


class ItemTag(BaseModel):
    """Model to track the tags of inventory items."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    id: int
    """The unique identifier of the item tag."""

    name: str
    """The name of the tag."""

    tag_group: Optional[int] = None
    """The tag group the tag is associated with."""

    description: Optional[str]
    """The description of the tag."""

    creation_date: Optional[datetime] = datetime.now()
    """The creation date of the tag."""

    last_change: Optional[datetime] = datetime.now()
    """The last change date of the tag."""
