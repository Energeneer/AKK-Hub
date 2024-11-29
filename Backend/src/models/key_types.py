# Backend/src/models/key_types.py
# Definition of the Key Type model: What types of keys are available for the system

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


class KeyTypesTable(BaseTable):
    """Definition of the KeyTypes model for the database."""

    __tablename__ = "KeyTypes"
    Id = Column(Integer, primary_key=True)
    """The unique identifier of the key type."""

    Name = Column(String, nullable=False)
    """The name of the key type."""

    Description = Column(Text, nullable=True, default=None)
    """The description of the key type."""

    HangerNumber = Column(Integer, nullable=True, default=None)
    """The number of the key hanger within the key cabinet."""

    CreationDate = Column(DateTime, nullable=False, default=datetime.now())
    """The creation date of the key type."""

    LastChange = Column(DateTime, nullable=False, default=datetime.now())
    """The last change date of the key type."""


class KeyType(BaseModel):
    """Definition of the KeyTypes model for the API."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    id: int
    """The unique identifier of the key type."""

    name: str
    """The name of the key type."""

    description: Optional[str]
    """The description of the key type."""

    hanger_number: Optional[int]
    """The number of the key hanger within the key cabinet."""

    creation_date: Optional[datetime] = datetime.now()
    """The creation date of the key type."""

    last_change: Optional[datetime] = datetime.now()
    """The last change date of the key type."""
