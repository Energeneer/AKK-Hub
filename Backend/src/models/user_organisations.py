# Backend/src/models/user_organisations.py
# Definition of the UserOrganisation model, connecting users and organisations

# Author: Valentin Haas, 2024

# Library imports
from sqlalchemy import Column, Integer

# Project imports
from ._base import BaseTable


class UserOrganisationsTable(BaseTable):
    """Definition of the UserOrganisation model for the database."""

    __tablename__ = "UserOrganisations"

    User = Column(Integer, primary_key=True, foreign_key="Users.Id")
    """The unique identifier of the user."""

    Organisation = Column(Integer, primary_key=True, foreign_key="Organisations.Id")
    """The unique identifier of the organisation."""
