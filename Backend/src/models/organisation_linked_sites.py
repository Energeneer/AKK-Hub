# Backend/src/models/organisation_linked_sites.py
# Definition of the OrganisationLinkedSite model, connecting Organisations and linked sites

# Author: Valentin Haas, 2024

# Library imports
from sqlalchemy import Column, Integer

# Project imports
from ._base import BaseTable


class OrganisationLinkedSitesTable(BaseTable):
    """Definition of the OrganisationLinkedSite model for the database."""

    __tablename__ = "OrganisationLinkedSites"

    Organisation = Column(Integer, primary_key=True, foreign_key="Organisations.Id")
    """The unique identifier of the Organisation."""

    Site = Column(Integer, primary_key=True, foreign_key="LinkedSites.Id")
    """The unique identifier of the linked site."""
