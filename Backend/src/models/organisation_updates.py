# Backend/src/models/organisation_updates.py
# Definition of the OrganisationUpdate model, tracking updates to organisations

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

# Project imports
from .updates import UpdateType


class OrganisationUpdatesTable(BaseTable):
    """Model to track the updates of organisations."""

    __tablename__ = "OrganisationUpdates"
    Id = Column(Integer, primary_key=True)
    """The unique identifier of the organisation update."""

    Organisation = Column(Integer, nullable=False)
    """The organisation affected by the update."""

    Time = Column(DateTime, nullable=False)
    """The time of the update."""

    Type = Column(Enum(UpdateType), nullable=False)
    """The type of the update."""

    Title = Column(String, nullable=False)
    """The title of the update."""

    UpdatedBy = Column(Integer, nullable=False, foreign_key="Users.Id")
    """The user who updated the organisation."""

    Text = Column(Text, nullable=True, default=None)
    """The text of the update."""

    def to_pydantic(self):
        return super().to_pydantic(self, OrganisationUpdate)


class OrganisationUpdate(BaseModel):
    """Model to track the updates of organisations."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    id: int
    """The unique identifier of the organisation update."""

    organisation: int
    """The organisation affected by the update."""

    time: datetime
    """The time of the update."""

    type: UpdateType
    """The type of the update."""

    title: str
    """The title of the update."""

    updated_by: int
    """The user reference who updated the organisation."""

    text: Optional[str] = None
    """The text of the update."""
