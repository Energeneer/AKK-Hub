# Backend/src/models/address_tel_numbers.py
# Definition of the AddressTelNumbers model that connects addresses and telefone numbers.

# Author: Valentin Haas, 2024

# System imports
from typing import Optional

# Library imports
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_pascal
from sqlalchemy import Column, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base

# Constants
BASE = declarative_base()


class AddressTelNumbersTable(BASE):
    """Definition of the AddressTelNumbers model for the database."""

    __tablename__ = "AddressTelNumbers"

    Address = Column(Integer, primary_key=True, foreign_key="Addresses.Id")
    """The unique identifier of the address."""

    TelNumber = Column(Integer, primary_key=True, foreign_key="TelefoneNumbers.Id")
    """The unique identifier of the telefone number."""

    IsPrimary = Column(Boolean, nullable=False, default=True)
    """Indicates whether the telefone number is the primary telefone number for the address."""


class AddressTelNumber(BaseModel):
    """Definition of the AddressTelNumber model for the API."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    address: int
    """The unique identifier of the address."""

    tel_number: int
    """The unique identifier of the telefone number."""

    is_primary: Optional[bool] = True
    """Indicates whether the telefone number is the primary telefone number for the address."""
