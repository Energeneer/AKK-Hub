# Backend/src/models/linked_sites.py
# Definition of the LinkedSite model to represent external websites of entities

# Author: Valentin Haas, 2024

# System imports
from datetime import datetime
from typing import Optional

# Library imports
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_pascal
from sqlalchemy import Column, Integer, DateTime, String

# Project imports
from ._base import BaseTable


class LinkedSitesTable(BaseTable):
    """Definition of the LinkedSite model for the database."""

    __tablename__ = "LinkedSites"
    Id = Column(Integer, primary_key=True)
    """The unique identifier of the linked site."""

    Name = Column(String, nullable=False)
    """The name of the linked site."""

    Link = Column(String, nullable=False)
    """The link to the linked site."""

    IconPath = Column(String, nullable=True)
    """The path to the icon of the linked site."""

    CreationDate = Column(DateTime, nullable=False, default=datetime.now())
    """The creation date of the linked site."""


class LinkedSite(BaseModel):
    """Definition of the LinkedSite model for the API."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    id: int
    """The unique identifier of the linked site."""

    name: str
    """The name of the linked site."""

    link: str
    """The link to the linked site."""

    icon_path: Optional[str]
    """The path to the icon of the linked site."""

    creation_date: datetime
    """The creation date of the linked site."""
