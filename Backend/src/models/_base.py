# Backend/src/models/_base.py
# Base class for all database models, providing common functionality.

# Author: Valentin Haas, 2024

# Library imports
from sqlmodel import SQLModel
from pydantic import ConfigDict
    
class BaseModel(SQLModel):
    """Base class for all models, providing common functionality and configuration."""
    
    # Do not generate a table for the base model
    __abstract__ = True

    # Generak pydantic configuration for all models
    model_config = ConfigDict(populate_by_name=True)
