# Backend/src/models/_base.py
# Base class for all database models, providing common functionality.

# Author: Valentin Haas, 2024

# System imports
from typing import Type, TypeVar

# Library imports
from pydantic import BaseModel
from sqlalchemy.orm import DeclarativeBase

# Constants
T = TypeVar("T", bound=BaseModel)


# declarative base class
class BaseTable(DeclarativeBase):
    """Base class for all SQLAlchemy database models, providing common functionality."""

    __abstract__ = True

    @staticmethod
    def to_pydantic(db_object: "BaseTable", pydantic_model: Type[T]) -> T:
        """
        Convert a database object to a Pydantic model.

        Args:
            db_object (BaseTable): The database object to convert.
            pydantic_model (Type[T]): The Pydantic model to convert to.

        Returns:
            T: The Pydantic model, filled with the data from the database object.
        """
        return pydantic_model(**db_object.__dict__)
