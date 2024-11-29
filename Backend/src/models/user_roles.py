# Backend/src/models/user_roles.py
# Many to Many relationship between users and roles

# Author: Valentin Haas, 2024

# Library imports
from sqlalchemy import Column, Integer

# Project imports
from ._base import BaseTable


class UserRolesTable(BaseTable):
    """Model to track the relationship between users and roles."""

    __tablename__ = "UserRoles"

    User = Column(Integer, primary_key=True, foreign_key="Users.Id")
    """The user in the relationship."""

    Role = Column(Integer, primary_key=True, foreign_key="Roles.Id")
    """The role in the relationship."""
