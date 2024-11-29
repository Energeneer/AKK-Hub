# Backend/src/models/lock_updates.py
# Definition of the LockUpdate model, tracking updates to locks

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


class LockUpdatesTable(BaseTable):
    """Model to track the updates of locks."""

    __tablename__ = "LockUpdates"
    Id = Column(Integer, primary_key=True)
    """The unique identifier of the lock update."""

    Lock = Column(Integer, nullable=False)
    """The lock affected by the update."""

    Time = Column(DateTime, nullable=False)
    """The time of the update."""

    Type = Column(Enum(UpdateType), nullable=False)
    """The type of the update."""

    Title = Column(String, nullable=False)
    """The title of the update."""

    UpdatedBy = Column(Integer, nullable=False, foreign_key="Locks.Id")
    """The user who updated the lock."""

    Text = Column(Text, nullable=True, default=None)
    """The text of the update."""

    def to_pydantic(self):
        return super().to_pydantic(self, LockUpdate)


class LockUpdate(BaseModel):
    """Model to track the updates of locks."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    id: int
    """The unique identifier of the lock update."""

    lock: int
    """The lock affected by the update."""

    time: datetime
    """The time of the update."""

    type: UpdateType
    """The type of the update."""

    title: str
    """The title of the update."""

    updated_by: int
    """The user who updated the lock."""

    text: Optional[str] = None
    """The text of the update."""
