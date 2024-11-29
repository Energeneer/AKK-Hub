# Backend/src/models/users.py
# Definition of the User model

# Author: Valentin Haas, 2024

# System imports
from datetime import datetime
from typing import Optional

# Library imports
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_pascal
from sqlalchemy import Boolean, Column, Date, DateTime, Integer, String, Text

# Project imports
from ._base import BaseTable


class UsersTable(BaseTable):
    """Definition of the User model for the database."""

    __tablename__ = "Users"
    Id = Column(Integer, primary_key=True)
    """The unique identifier of the user."""

    Nickname = Column(String, nullable=False)
    """The nickname of the user."""

    Username = Column(String, unique=True, nullable=True, default=None)
    """The username of the user."""

    PasswordHash = Column(String, nullable=True, default=None)
    """The hashed password of the user."""

    OAuthToken = Column(String, nullable=True, default=None)
    """The OAuth token of the user when using OAuth authentication."""

    WebAuthToken = Column(String, nullable=True, default=None)
    """The web authentication token of the user for web authentication."""

    Title = Column(String, nullable=True, default=None)
    """The title of the user."""

    FirstName = Column(String, nullable=True, default=None)
    """The first name of the user."""

    MiddleNames = Column(String, nullable=True, default=None)
    """The middle names of the user."""

    LastName = Column(String, nullable=True, default=None)
    """The last name of the user."""

    Initials = Column(String, nullable=True, default=None)
    """The initials of the user."""

    Birthdate = Column(Date, nullable=True, default=None)
    """The birthdate of the user."""

    PublicImagePath = Column(String, nullable=True, default=None)
    """The path to the public image of the user."""

    InternalImagePath = Column(String, nullable=True, default=None)
    """The path to the internal image of the user."""

    Description = Column(Text, nullable=True, default=None)
    """The description of the user the user can set."""

    CreationDate = Column(DateTime, nullable=True, default=datetime.now())
    """The creation date of the user."""

    IsBlocked = Column(Boolean, nullable=False, default=False)
    """The blocked status of the user."""

    InternalRemark = Column(Text, nullable=True, default=None)
    """The internal remark of the user."""

    LastChange = Column(DateTime, nullable=False, default=datetime.now())
    """The last change of the user."""

    def to_pydantic(self):
        return super().to_pydantic(self, User)


class User(BaseModel):
    """Definition of the User model for the API."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    id: int
    """The unique identifier of the user."""

    nickname: str
    """The nickname of the user."""

    username: Optional[str] = None
    """The username of the user."""

    o_auth_token: Optional[str] = None
    """The OAuth token of the user when using OAuth authentication."""

    web_auth_token: Optional[str] = None
    """The web authentication token of the user for web authentication."""

    title: Optional[str] = None
    """The title of the user."""

    first_name: Optional[str] = None
    """The first name of the user."""

    middle_names: Optional[str] = None
    """The middle names of the user."""

    last_name: Optional[str] = None
    """The last name of the user."""

    initials: Optional[str] = None
    """The initials of the user."""

    birthdate: Optional[datetime] = None
    """The birthdate of the user."""

    public_image_path: Optional[str] = None
    """The path to the public image of the user."""

    internal_image_path: Optional[str] = None
    """The path to the internal image of the user."""

    description: Optional[str] = None
    """The description of the user the user can set."""

    creation_date: Optional[datetime] = datetime.now()
    """The creation date of the user."""

    is_blocked: bool = False
    """The blocked status of the user."""

    internal_remark: Optional[str] = None
    """The internal remark of the user."""

    last_change: datetime = datetime.now()
    """The last change of the user."""
