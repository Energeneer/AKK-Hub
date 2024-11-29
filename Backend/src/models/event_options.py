# Backend/src/models/event_options.py
# Definition of the EventOptions model, tracking the options for events.

# Author: Valentin Haas, 2024

# System imports
from datetime import datetime
from typing import Optional

# Library imports
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_pascal
from sqlalchemy import Column, Integer, DateTime, String, Text

# Project imports
from ._base import BaseTable


class EventOptionsTable(BaseTable):
    """Model to track the options for events."""

    __tablename__ = "EventOptions"
    Id = Column(Integer, primary_key=True)
    """The unique identifier of the event option."""

    Event = Column(Integer, nullable=False, foreign_key="Events.Id")
    """The event that the option belongs to."""

    Title = Column(String, nullable=False)
    """The title of the option."""

    CostCt = Column(Integer, nullable=False)
    """The cost of the option in cents."""

    Description = Column(Text, nullable=True, default=None)
    """The description of the option."""

    IsOptional = Column(Integer, nullable=False, default=True)
    """Whether the option is optional or not."""

    CreationDate = Column(DateTime, nullable=False, default=datetime.now())
    """The date when the option was created."""

    LastChange = Column(DateTime, nullable=False, default=datetime.now())
    """The date when the option was last changed."""

    def to_pydantic(self):
        return super().to_pydantic(self, EventOption)


class EventOption(BaseModel):
    """Model to track the options for events."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    id: int
    """The unique identifier of the event option."""

    event: int
    """The event reference that the option belongs to."""

    title: str
    """The title of the option."""

    cost_ct: int
    """The cost of the option in cents."""

    description: Optional[str]
    """The description of the option."""

    is_optional: Optional[bool] = True
    """Whether the option is optional or not."""

    creation_date: Optional[datetime] = datetime.now()
    """The date when the option was created."""

    last_change: Optional[datetime] = datetime.now()
    """The date when the option was last changed."""
