# Backend/src/models/user_groups.py
# Many to Many relationship between users and groups

# Author: Valentin Haas, 2024

# Library imports
from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

# Constants
BASE = declarative_base()


class UserGroupsTable(BASE):
    """Model to track the relationship between users and groups."""

    __tablename__ = "UserGroups"

    User = Column(Integer, primary_key=True, foreign_key="Users.Id")
    """The user in the relationship."""

    Group = Column(Integer, primary_key=True, foreign_key="Groups.Id")
    """The group in the relationship."""
