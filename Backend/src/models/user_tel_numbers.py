# Backend/src/models/user_tel_numbers.py
# Definition of the UserTelNumber model, connecting users and telephone numbers

# Author: Valentin Haas, 2024

# Library imports
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_pascal
from sqlalchemy import Boolean, Column, Integer

# Project imports
from ._base import BaseTable


class UserTelNumbersTable(BaseTable):
    """Definition of the UserTelNumber model for the database."""

    __tablename__ = "UserTelNumbers"

    User = Column(Integer, primary_key=True, foreign_key="Users.Id")
    """The unique identifier of the user."""

    TelNumber = Column(Integer, primary_key=True, foreign_key="TelephoneNumbers.Id")
    """The unique identifier of the telephone number."""

    IsPrimary = Column(Boolean, nullable=False, default=False)
    """Whether the telephone number is the primary telephone number of the user."""


class UserTelNumber(BaseModel):
    """Definition of the UserTelNumber model for the API."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    user: int
    """The unique identifier of the user."""

    tel_number: int
    """The unique identifier of the telephone number."""

    is_primary: bool
    """Whether the telephone number is the primary telephone number of the user."""
