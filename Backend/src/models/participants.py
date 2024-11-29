# Backend/src/models/participants.py
# Definition of the Participant model, tracking participants in events.

# Author: Valentin Haas, 2024

# System imports
from datetime import datetime
from typing import Optional
import enum

# Library imports
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_pascal
from sqlalchemy import Boolean, Column, DateTime, Enum, Integer

# Project imports
from ._base import BaseTable


class ParticipantRoles(enum.Enum):
    """Enum to define the roles of participants in events."""

    OTHER = 0
    """The participant has another role in the event."""

    ORGANIZER = 1
    """The participant is an organizer of the event."""

    SEPAKER = 2
    """The participant is a speaker at the event."""

    PARTICIPANT = 3
    """The participant is a participant in the event."""

    VISITOR = 4
    """The participant is a visitor of the event."""

    BAND = 5
    """The participant is a band at the event."""

    SPONSOR = 6
    """The participant is a sponsor of the event."""


class ParticipantsTable(BaseTable):
    """Model to track participants in events."""

    __tablename__ = "Participants"

    User = Column(Integer, primary_key=True, foreign_key="Users.Id")
    """The unique identifier of the user."""

    Event = Column(Integer, primary_key=True, foreign_key="Events.Id")
    """The unique identifier of the event."""

    Role = Column(Enum(ParticipantRoles), nullable=False)
    """The role of the participant in the event."""

    Organisation = Column(Integer, nullable=True, foreign_key="Organisations.Id")
    """The organisation of the participant in the event."""

    ChosenItems = Column(Integer, nullable=True, foreign_key="EventOptions.Id")
    """The chosen items of the participant in the event."""

    PayedAmountCt = Column(Integer, nullable=False, default=0)
    """The amount payed by the participant in cents."""

    HasAcceptedEventRequirements = Column(Boolean, nullable=False, default=False)
    """Indicates whether the participant has accepted the event requirements."""

    CreationDate = Column(DateTime, nullable=False, default=datetime.now())
    """The creation date of the participant."""

    LastChange = Column(DateTime, nullable=False, default=datetime.now())
    """The last change date of the participant."""


class Participant(BaseModel):
    """Definition of the Participant model."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    user: int
    """The unique identifier of the user."""

    event: int
    """The unique identifier of the event."""

    role: int
    """The role of the participant in the event."""

    organisation: Optional[int]
    """The organisation of the participant in the event."""

    chosen_items: Optional[int]
    """The chosen items of the participant in the event."""

    payed_amount_ct: int
    """The amount payed by the participant in cents."""

    has_accepted_event_requirements: bool
    """Indicates whether the participant has accepted the event requirements."""

    creation_date: datetime
    """The creation date of the participant."""

    last_change: datetime
    """The last change date of the participant."""
