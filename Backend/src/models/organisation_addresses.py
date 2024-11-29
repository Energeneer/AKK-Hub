# /Backend/src/models/organisation_addresses.py
# Definition of the OrganisationAddress model, connecting Organisations and Addresses

# Author: Valentin Haas, 2024

# System imports
from datetime import datetime
from typing import Optional

# Library imports
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_pascal
from sqlalchemy import Boolean, Column, DateTime, Integer

# Project imports
from ._base import BaseTable


class OrganisationAddressesTable(BaseTable):
    """Model to connect Organisations and Addresses."""

    __tablename__ = "OrganisationAddresses"

    Organisation = Column(Integer, primary_key=True, foreign_key="Organisations.Id")
    """The unique identifier of the organisation."""

    Address = Column(Integer, primary_key=True, foreign_key="Addresses.Id")
    """The unique identifier of the address."""

    IsPrimary = Column(Boolean, nullable=False, default=True)
    """Indicates whether the address is the primary address for the organisation."""

    CreationDate = Column(DateTime, nullable=False, default=datetime.now())
    """The creation date of the connection."""


class OrganisationAddress(BaseModel):
    """Model to connect Organisations and Addresses."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    organisation: int
    """The unique identifier of the organisation."""

    address: int
    """The unique identifier of the address."""

    is_primary: Optional[bool] = True
    """Indicates whether the address is the primary address for the organisation."""

    creation_date: datetime
    """The creation date of the connection."""
