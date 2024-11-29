# Backend/src/models/users.py
# Definition of the User model

# Author: Valentin Haas, 2024

# System imports
from datetime import datetime
from typing import Optional

# Library imports
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_pascal
from sqlalchemy import Column, Integer, Date, DateTime, String, Text, Boolean

# Project imports
from ._base import BaseTable


class OrganisationsTable(BaseTable):
    """Definition of the Organisation model for the database."""

    __tablename__ = "Organisations"
    Id = Column(Integer, primary_key=True)
    """The unique identifier of the organisation."""

    Name = Column(String, nullable=False, unique=True)
    """The name of the organisation."""

    Description = Column(Text, nullable=True, default=None)
    """The description of the organisation."""

    IsStudentic = Column(Boolean, nullable=False, default=False)
    """Whether the organisation is a Studentic organisation."""

    CreationDate = Column(DateTime, nullable=False, default=datetime.now())
    """The creation date of the organisation."""

    IsBlocked = Column(Boolean, nullable=False, default=True)
    """Whether the organisation is blocked."""

    InternalRemark = Column(Text, nullable=True, default=None)
    """An internal remark about the organisation."""

    LastUpdate = Column(DateTime, nullable=False, default=datetime.now())


class Organisation(BaseModel):
    """Definition of the Organisation model for the API."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    id: int
    """The unique identifier of the organisation."""

    name: str
    """The name of the organisation."""

    description: Optional[str] = None
    """The description of the organisation."""

    is_studentic: bool = False
    """Whether the organisation is a Studentic organisation."""

    creation_date: datetime = datetime.now()
    """The creation date of the organisation."""

    is_blocked: bool = True
    """Whether the organisation is blocked."""

    internal_remark: Optional[str] = None
    """An internal remark about the organisation."""

    last_update: datetime = datetime.now()
    """The last update date of the organisation."""
