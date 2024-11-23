# Backend/src/models/organisation_emails.py
# Definition of the OrganisationEmail model, connecting organisations and emails

# Author: Valentin Haas, 2024

# Library imports
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_pascal
from sqlalchemy import Column, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base

# Constants
BASE = declarative_base()


class OrganisationEmailsTable(BASE):
    """Definition of the OrganisationEmail model for the database."""

    __tablename__ = "OrganisationEmails"

    Organisation = Column(Integer, primary_key=True, foreign_key="Organisations.Id")
    """The unique identifier of the organisation."""

    Email = Column(Integer, primary_key=True, foreign_key="Emails.Id")
    """The unique identifier of the email."""

    IsPrimary = Column(Boolean, nullable=False, default=False)
    """Whether the email is the primary email of the organisation."""


class OrganisationEmail(BaseModel):
    """Definition of the OrganisationEmail model for the API."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    organisation: int
    """The unique identifier of the organisation."""

    email: int
    """The unique identifier of the email."""

    is_primary: bool
    """Whether the email is the primary email of the organisation."""
