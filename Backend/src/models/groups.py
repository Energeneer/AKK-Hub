# Backend/src/models/groups.py
# Definition of the Group model, tracking groups of users

# Author: Valentin Haas, 2024

# System imports
from typing import Optional

# Library imports
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_pascal
from sqlalchemy import Column, Integer, String, Text

# Project imports
from ._base import BaseTable


class GroupsTable(BaseTable):
    """Model to track the groups of users."""

    __tablename__ = "Groups"
    Id = Column(Integer, primary_key=True)
    """The unique identifier of the group."""

    Name = Column(String, nullable=False)
    """The name of the group."""

    Description = Column(Text, nullable=True, default=None)
    """The description of the group."""


class Group(BaseModel):
    """Model to track the groups of users."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    id: int
    """The unique identifier of the group."""

    name: str
    """The name of the group."""

    description: Optional[str]
    """The description of the group."""
