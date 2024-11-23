# Backend/src/models/telephone_numbers.py
# Definition of the TelephoneNumber model

# Author: Valentin Haas, 2024

# System imports
from datetime import datetime
from enum import Enum

# Library imports
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_pascal
from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.ext.declarative import declarative_base

# Constants
BASE = declarative_base()


class TelephoneNumberType(Enum):
    """The type of the telephone number."""

    OTHER = 0
    """The telephone number is of another type."""

    HOME = 1
    """The telephone number is a home number."""

    MOBILE = 2
    """The telephone number is a mobile number."""

    WORK = 3
    """The telephone number is a work number."""

    FAX = 4
    """The telephone number is a fax number."""


class TelephoneNumbersTable(BASE):
    """Definition of the TelephoneNumber model for the database."""

    __tablename__ = "TelephoneNumbers"
    Id = Column(Integer, primary_key=True)
    """The unique identifier of the telephone number."""

    Number = Column(String, nullable=False)
    """The number of the telephone number."""

    Label = Column(String, nullable=False)
    """The label of the telephone number."""

    Type = Column(Integer, nullable=False)
    """The type of the telephone number."""

    CreationDate = Column(DateTime, nullable=False, default=datetime.now)
    """The creation date of the telephone number."""


class TelephoneNumber(BaseModel):
    """Definition of the TelephoneNumber model for the API."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    id: int
    """The unique identifier of the telephone number."""

    number: str
    """The number of the telephone number."""

    label: str
    """The label of the telephone number."""

    type: TelephoneNumberType
    """The type of the telephone number."""

    creation_date: datetime
    """The creation date of the telephone number."""
