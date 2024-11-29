# Backend/src/models/user_emails.py
# Definition of the UserEmail model, connecting users and emails

# Author: Valentin Haas, 2024

# Library imports
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_pascal
from sqlalchemy import Column, Integer, Boolean

# Project imports
from ._base import BaseTable


class UserEmailsTable(BaseTable):
    """Definition of the UserEmail model for the database."""

    __tablename__ = "UserEmails"

    User = Column(Integer, primary_key=True, foreign_key="Users.Id")
    """The unique identifier of the user."""

    Email = Column(Integer, primary_key=True, foreign_key="Emails.Id")
    """The unique identifier of the email."""

    IsPrimary = Column(Boolean, nullable=False, default=False)
    """Whether the email is the primary email of the user."""


class UserEmail(BaseModel):
    """Definition of the UserEmail model for the API."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    user: int
    """The unique identifier of the user."""

    email: int
    """The unique identifier of the email."""

    is_primary: bool
    """Whether the email is the primary email of the user."""
