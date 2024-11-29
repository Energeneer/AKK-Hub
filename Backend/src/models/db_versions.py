# Backend/src/models/db_versions.py
# Model to track the database version history

# Valentin Haas, 2024

# System imports
from datetime import datetime
from typing import Optional

# Library imports
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_pascal
from sqlalchemy import Column, Integer, DateTime, String, Text

# Project imports
from ._base import BaseTable


class DBVersionsTable(BaseTable):
    """Model to track the database version history."""

    __tablename__ = "DBVersions"
    DatabaseVersion = Column(Integer, primary_key=True)
    """The version of the database schema."""

    Time = Column(DateTime, nullable=False)
    """The time when the database schema was updated."""

    ProductVersion = Column(String, nullable=False)
    """The version of the product that was released with this database schema."""

    Description = Column(Text, nullable=True)
    """A description of the changes made in this database schema."""


class DBVersion(BaseModel):
    """Model to track the database version history."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    database_version: int
    """The version of the database schema."""

    time: datetime
    """The time when the database schema was updated."""

    product_version: str
    """The version of the product that was released with this database schema."""

    description: Optional[str] = None
    """A description of the changes made in this database schema."""
