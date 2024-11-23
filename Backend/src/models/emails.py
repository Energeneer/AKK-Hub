# Backend/src/models/emails.py
# Definition of the Email model

# Author: Valentin Haas, 2024

# System imports
from datetime import datetime

# Library imports
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_pascal
from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.ext.declarative import declarative_base

# Constants
BASE = declarative_base()


class EmailsTable(BASE):
    """Definition of the Email model for the database."""

    __tablename__ = "Emails"
    Id = Column(Integer, primary_key=True)
    """The unique identifier of the email."""

    Address = Column(String, nullable=False)
    """The address of the email."""

    Label = Column(String, nullable=False)
    """The label of the email."""

    CreationDate = Column(DateTime, nullable=False, default=datetime.now)
    """The creation date of the email."""


class Email(BaseModel):
    """Definition of the Email model for the API."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    id: int
    """The unique identifier of the email."""

    address: str
    """The address of the email."""

    label: str
    """The label of the email."""

    creation_date: datetime
    """The creation date of the email."""
