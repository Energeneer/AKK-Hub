# Backend/src/models/address_emails.py
# Definition of the AddressEmails model that connects addresses and emails.

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


class AddressEmailsTable(BASE):
    """Definition of the AddressEmails model for the database."""

    __tablename__ = "AddressEmails"

    Address = Column(Integer, primary_key=True, foreign_key="Addresses.Id")
    """The unique identifier of the address."""

    Email = Column(Integer, primary_key=True, foreign_key="Emails.Id")
    """The unique identifier of the email."""

    IsPrimary = Column(Boolean, nullable=False, default=True)
    """Indicates whether the email is the primary email for the address."""


class AddressEmail(BaseModel):
    """Definition of the AddressEmail model for the API."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    address: int
    """The unique identifier of the address."""

    email: int
    """The unique identifier of the email."""

    is_primary: Optional[bool] = True
    """Indicates whether the email is the primary email for the address."""
