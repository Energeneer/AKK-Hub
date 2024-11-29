# Backend/src/models/roles.py
# Definition of the Role model, tracking roles of users

# Author: Valentin Haas, 2024

# System imports
from typing import Optional

# Library imports
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_pascal
from sqlalchemy import Column, Integer, String, Text

# Project imports
from ._base import BaseTable


class RolesTable(BaseTable):
    """Model to track the roles of users."""

    __tablename__ = "Roles"
    Id = Column(Integer, primary_key=True)
    """The unique identifier of the role."""

    Name = Column(String, nullable=False)
    """The name of the role."""

    Description = Column(Text, nullable=True, default=None)
    """The description of the role."""

    def to_pydantic(self):
        return super().to_pydantic(self, Role)


class Role(BaseModel):
    """Model to track the roles of users."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    id: int
    """The unique identifier of the role."""

    name: str
    """The name of the role."""

    description: Optional[str]
    """The description of the role."""
