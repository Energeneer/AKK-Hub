# /Backend/src/models/user_addresses.py
# Definition of the UserAddress model, connecting Users and Addresses

# Author: Valentin Haas, 2024

# System imports
from datetime import datetime
from typing import Optional

# Library imports
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_pascal
from sqlalchemy import Boolean, Column, Integer, DateTime

# Project imports
from ._base import BaseTable


class UserAddressesTable(BaseTable):
    """Model to connect Users and Addresses."""

    __tablename__ = "UserAddresses"

    User = Column(Integer, primary_key=True, foreign_key="Users.Id")
    """The unique identifier of the user."""

    Address = Column(Integer, primary_key=True, foreign_key="Addresses.Id")
    """The unique identifier of the address."""

    IsPrimary = Column(Boolean, nullable=False, default=True)
    """Indicates whether the address is the primary address for the user."""

    CreationDate = Column(DateTime, nullable=False, default=datetime.now())
    """The creation date of the connection."""


class UserAddress(BaseModel):
    """Model to connect Users and Addresses."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    user: int
    """The unique identifier of the user."""

    address: int
    """The unique identifier of the address."""

    is_primary: Optional[bool] = True
    """Indicates whether the address is the primary address for the user."""

    creation_date: datetime
    """The creation date of the connection."""
