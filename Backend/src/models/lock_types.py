# Backend/src/models/lock_types.py
# Definition of the LockType model

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


class LockTypesTable(BaseTable):
    """Definition of the LockType model for the database."""

    __tablename__ = "LockTypes"
    Id = Column(Integer, primary_key=True)
    """The unique identifier of the lock type."""

    Name = Column(String, nullable=False)
    """The name of the lock type."""

    Description = Column(Text, nullable=True, default=None)
    """The description of the lock type."""

    CreationDate = Column(DateTime, nullable=False, default=datetime.now())
    """The creation date of the lock type."""

    LastChange = Column(DateTime, nullable=False, default=datetime.now())
    """The last change date of the lock type."""


class LockType(BaseModel):
    """Definition of the LockType model for the API."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    id: int
    """The unique identifier of the lock type."""

    name: str
    """The name of the lock type."""

    description: Optional[str] = None
    """The description of the lock type."""

    creation_date: Optional[datetime] = datetime.now()
    """The creation date of the lock type."""

    last_change: Optional[datetime] = datetime.now()
    """The last change date of the lock type."""
