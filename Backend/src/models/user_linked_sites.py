# Backend/src/models/user_linked_sites.py
# Definition of the UserLinkedSite model, connecting users and linked sites

# Author: Valentin Haas, 2024

# Library imports
from sqlalchemy import Column, Integer

# Project imports
from ._base import BaseTable


class UserLinkedSitesTable(BaseTable):
    """Definition of the UserLinkedSite model for the database."""

    __tablename__ = "UserLinkedSites"

    User = Column(Integer, primary_key=True, foreign_key="Users.Id")
    """The unique identifier of the user."""

    Site = Column(Integer, primary_key=True, foreign_key="LinkedSites.Id")
    """The unique identifier of the linked site."""
