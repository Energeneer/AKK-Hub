# Backend/src/models/addresses.py
# Definition of the Address model

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


class AddressesTable(BASE):
    """Definition of the Address model for the database."""

    __tablename__ = "Addresses"
    Id = Column(Integer, primary_key=True)
    """The unique identifier of the address."""

    StreetName = Column(String, nullable=False)
    """The name of the street of the address."""

    HouseNumber = Column(String, nullable=False)
    """The house number of the address."""

    AddressLine2 = Column(String, nullable=True, default=None)
    """The second line of the address."""

    ZipCode = Column(String, nullable=False)
    """The ZIP code of the address."""

    City = Column(String, nullable=False)
    """The city of the address."""

    Country = Column(String, nullable=False)
    """The country of the address."""

    Notes = Column(String, nullable=True, default=None)
    """Additional notes for the address."""

    CreationDate = Column(DateTime, nullable=False, default=datetime.now)
    """The creation date of the address."""

    LastChange = Column(DateTime, nullable=False, default=datetime.now)
    """The last change date of the address."""


class Address(BaseModel):
    """Definition of the Address model for the API."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    id: int
    """The unique identifier of the address."""

    street_name: str
    """The name of the street of the address."""

    house_number: str
    """The house number of the address."""

    address_line_2: Optional[str] = None
    """The second line of the address."""

    zip_code: str
    """The ZIP code of the address."""

    city: str
    """The city of the address."""

    country: str
    """The country of the address."""

    notes: Optional[str] = None
    """Additional notes for the address."""

    creation_date: datetime
    """The creation date of the address."""

    last_change: datetime
    """The last change date of the address."""
