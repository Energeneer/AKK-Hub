# Backend/src/models/organisation_tel_numbers.py
# Definition of the OrganisationTelNumber model, connecting organisations and telephone numbers

# Author: Valentin Haas, 2024

# Library imports
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_pascal
from sqlalchemy import Column, Integer, Boolean

# Project imports
from ._base import BaseTable


class OrganisationTelNumbersTable(BaseTable):
    """Definition of the OrganisationTelNumber model for the database."""

    __tablename__ = "OrganisationTelNumbers"

    Organisation = Column(Integer, primary_key=True, foreign_key="Organisations.Id")
    """The unique identifier of the organisation."""

    TelNumber = Column(Integer, primary_key=True, foreign_key="TelephoneNumbers.Id")
    """The unique identifier of the telephone number."""

    IsPrimary = Column(Boolean, nullable=False, default=False)
    """Whether the telephone number is the primary telephone number of the organisation."""


class OrganisationTelNumber(BaseModel):
    """Definition of the OrganisationTelNumber model for the API."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    organisation: int
    """The unique identifier of the organisation."""

    tel_number: int
    """The unique identifier of the telephone number."""

    is_primary: bool
    """Whether the telephone number is the primary telephone number of the organisation."""
