# Backend/src/models/user_roles.py
# Many to Many relationship between users and roles

# Author: Valentin Haas, 2024

# Library imports
from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

# Constants
BASE = declarative_base()


class UserRolesTable(BASE):
    """Model to track the relationship between users and roles."""

    __tablename__ = "UserRoles"

    User = Column(Integer, primary_key=True, foreign_key="Users.Id")
    """The user in the relationship."""

    Role = Column(Integer, primary_key=True, foreign_key="Roles.Id")
    """The role in the relationship."""
