# Backend/src/models/keys.py
# Definition of the Key model

# Author: Valentin Haas, 2024

# System imports
from datetime import datetime
from typing import Optional

# Library imports
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_pascal
from sqlalchemy import Column, Integer, Date, DateTime, String, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base

# Constants
BASE = declarative_base()

# // Individual keys
# Table Keys {
#   Id uint [primary key]
#   Type uint [ref: > KeyTypes.Id]
#   Number smallint [unique]
#   CurrentOwner uuid [ref: > Users.Id]
#   DefaultLocation uint [ref: > RoomLocations.Id]
#   CurrentLocation uint [ref: > RoomLocations.Id]
#   DateReceived datetime
#   DateReturned datetime
#   LastAction nvarchar
#   LastActionComment text
#   CreationDate datetime
#   LastChange datetime
# }


class KeysTable(BASE):
    """Definition of the Keys model for the database."""

    __tablename__ = "Keys"
    Id = Column(Integer, primary_key=True)
    """The unique identifier of the key."""

    Type = Column(Integer, nullable=False, foreign_key="KeyTypes.Id")
    """The type of the key."""

    Number = Column(Integer, nullable=False, unique=True)
    """The number of the key."""

    CurrentOwner = Column(Integer, nullable=True, foreign_key="Users.Id")
    """The current owner of the key."""

    DefaultLocation = Column(Integer, nullable=False, foreign_key="RoomLocations.Id")
    """The default location of the key."""

    CurrentLocation = Column(Integer, nullable=True, foreign_key="RoomLocations.Id")
    """The current location of the key."""

    ReceiveByDate = Column(DateTime, nullable=True, default=datetime.now())
    """The date the key will be received."""

    ReceivedByDate = Column(DateTime, nullable=True, default=None)
    """The date the key was received."""

    ReturnByDate = Column(DateTime, nullable=True, default=None)
    """The date the key has to be returned."""

    ReturnedByDate = Column(DateTime, nullable=True, default=None)
    """The date the key was returned."""

    CreationDate = Column(DateTime, nullable=False, default=datetime.now())
    """The creation date of the key."""

    LastChange = Column(DateTime, nullable=False, default=datetime.now())
    """The last change date of the key."""


class Key(BaseModel):
    """Definition of the Keys model for the API."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    id: int
    """The unique identifier of the key."""

    type: int
    """The type of the key."""

    number: int
    """The number of the key."""

    current_owner: Optional[int] = None
    """The current owner of the key."""

    default_location: int
    """The default location of the key."""

    current_location: Optional[int] = None
    """The current location of the key."""

    receive_by_date: Optional[datetime] = datetime.now()
    """The date the key will be received."""

    received_by_date: Optional[datetime] = None
    """The date the key was received."""

    return_by_date: Optional[datetime] = None
    """The date the key has to be returned."""

    returned_by_date: Optional[datetime] = None
    """The date the key was returned."""

    creation_date: Optional[datetime] = datetime.now()
    """The creation date of the key."""

    last_change: Optional[datetime] = datetime.now()
    """The last change date of the key."""
