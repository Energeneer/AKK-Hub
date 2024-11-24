# Backend/src/models/buildings.py
# Description: Buildings model for storing building data

# Author: Valentin Haas, 2024

# System imports
from datetime import datetime
from typing import Optional

# Library imports
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_pascal
from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.ext.declarative import declarative_base

# Constants
BASE = declarative_base()


class BuildingsTable(BASE):
    """Definition of the Buildings model for the database."""

    __tablename__ = "Buildings"
    Id = Column(Integer, primary_key=True)
    """The unique identifier of the building."""

    Address = Column(Integer, nullable=False, foreign_key="Addresses.Id")
    """The address reference of the building."""

    Name = Column(String, nullable=False)
    """The name of the building."""

    Nickname = Column(String, nullable=True, default=None)
    """The nickname of the building."""

    CreationDate = Column(DateTime, nullable=False, default=datetime.now())
    """The creation date of the building entry."""


class Buildings(BaseModel):
    """Definition of the Buildings model for the API."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    id: int
    """The unique identifier of the building."""

    address: int
    """The address reference of the building."""

    Name: str
    """The name of the building."""

    Nickname: Optional[str]
    """The nickname of the building."""

    CreationDate: Optional[datetime] = datetime.now()
    """The creation date of the building entry."""
