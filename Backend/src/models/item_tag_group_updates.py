# Backend/src/models/item_tag_group_updates.py
# Definition of the ItemTagGroupUpdate model, tracking updates to item_tag_groups

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


class ItemTagGroupUpdatesTable(BASE):
    """Model to track the updates of item_tag_groups."""

    __tablename__ = "ItemTagGroupUpdates"
    Id = Column(Integer, primary_key=True)
    """The unique identifier of the item_tag_group update."""

    ItemTagGroup = Column(Integer, nullable=False)
    """The item_tag_group affected by the update."""

    Time = Column(DateTime, nullable=False)
    """The time of the update."""

    Type = Column(UpdateType, nullable=False)
    """The type of the update."""

    Title = Column(String, nullable=False)
    """The title of the update."""

    UpdatedBy = Column(Integer, nullable=False, foreign_key="ItemTagGroups.Id")
    """The item_tag_group who updated the item_tag_group."""

    Text = Column(Text, nullable=True, default=None)
    """The text of the update."""


class ItemTagGroupUpdate(BaseModel):
    """Model to track the updates of item_tag_groups."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    id: int
    """The unique identifier of the item_tag_group update."""

    item_tag_group: int
    """The item_tag_group affected by the update."""

    time: datetime
    """The time of the update."""

    type: UpdateType
    """The type of the update."""

    title: str
    """The title of the update."""

    updated_by: int
    """The item_tag_group who updated the item_tag_group."""

    text: Optional[str] = None
    """The text of the update."""
