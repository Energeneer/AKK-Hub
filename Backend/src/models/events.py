# Backend/src/models/events.py
# Definition of the Event model, tracking events

# Author: Valentin Haas, 2024

# System imports
from datetime import datetime
from enum import Enum
from typing import Optional

# Library imports
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_pascal
from sqlalchemy import Column, Integer, Date, DateTime, String, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base

# Constants
BASE = declarative_base()

# Table Events {
#   Id uint [primary key]
#   Title string
#   Description text
#   TimeFrame uint [ref:> TimeFrames.Id]
#   ExpectedPatricipantCount uint
#   EntryFeeCt uint
#   ExpectedCostsCt uint
#   ExpectedCostReasons text
#   IsStudentic bool
#   IsLiveMusicPlayed bool
#   IsGemaRequired bool
#   Organisation uint [ref: > Organisations.Id]
#   RoomReservation uint [ref: > RoomReservations.Id]
#   ItemReservation uint [ref: > ItemReservations.Id]
#   PosterPath image
#   PromoImagePath image
#   Type enum
#   Visibility enum
#   Status enum
#   ExternalRemarks text
#   InternalRemarks text
#   Requirements text
#   PublicationDate datetime
#   CreatedBy uint [ref: > Users.Id]
#   CreationDate datetime
#   LastChange datetime
# }


class EventType(Enum):
    """Enumeration of event types."""

    Other = 0
    """Other event type."""

    Meeting = 1
    """Meeting event type."""

    Workshop = 2
    """Workshop event type."""


class EventVisibility(Enum):
    """Enumeration of event visibilities."""

    Public = 0
    """Public event visibility."""

    Private = 1
    """Private event visibility."""

    Internal = 2
    """Internal event visibility."""


class EventStatus(Enum):
    """Enumeration of event statuses."""

    Draft = 0
    """Draft event status."""

    Published = 1
    """Published event status."""

    Cancelled = 2
    """Cancelled event status."""

    Deleted = 3
    """Deleted event status."""


class EventsTable(BASE):
    """Model to track events."""

    __tablename__ = "Events"
    Id = Column(Integer, primary_key=True)
    """The unique identifier of the event."""

    Title = Column(String, nullable=False)
    """The title of the event."""

    Description = Column(Text, nullable=True, default=None)
    """The description of the event."""

    TimeFrame = Column(Integer, nullable=False, foreign_key="TimeFrames.Id")
    """The time frame of the event."""

    ExpectedPatricipantCount = Column(Integer, nullable=False)
    """The expected number of participants."""

    EntryFeeCt = Column(Integer, nullable=False, default=0)
    """The entry fee in cents."""

    ExpectedCostsCt = Column(Integer, nullable=False, default=0)
    """The expected costs in cents."""

    ExpectedCostReasons = Column(Text, nullable=True, default=None)
    """The reasons for the expected costs."""

    IsStudentic = Column(Boolean, nullable=False, default=False)
    """Whether the event is a student initiative."""

    IsLiveMusicPlayed = Column(Boolean, nullable=False, default=False)
    """Whether live music is played at the event."""

    IsGemaRequired = Column(Boolean, nullable=False, default=False)
    """Whether GEMA is required for the event."""

    Organisation = Column(Integer, nullable=False, foreign_key="Organisations.Id")
    """The organisation responsible for the event."""

    RoomReservation = Column(Integer, nullable=False, foreign_key="RoomReservations.Id")
    """The room reservation for the event."""

    ItemReservation = Column(Integer, nullable=False, foreign_key="ItemReservations.Id")
    """The item reservation for the event."""

    PosterPath = Column(String, nullable=True, default=None)
    """The path to the poster image of the event."""

    PromoImagePath = Column(String, nullable=True, default=None)
    """The path to the promotional image of the event."""

    Type = Column(Enum, nullable=False)
    """The type of the event."""

    Visibility = Column(Enum, nullable=False)
    """The visibility of the event."""

    Status = Column(Integer, nullable=False)
    """The status of the event."""

    ExternalRemarks = Column(Text, nullable=True, default=None)
    """The external remarks of the event."""

    InternalRemarks = Column(Text, nullable=True, default=None)
    """The internal remarks of the event."""

    Requirements = Column(Text, nullable=True, default=None)
    """The requirements of the event."""

    PublicationDate = Column(DateTime, nullable=False, default=datetime.now())
    """The publication date of the event."""

    CreatedBy = Column(Integer, nullable=False, foreign_key="Users.Id")
    """The user who created the event."""

    CreationDate = Column(DateTime, nullable=False, default=datetime.now())
    """The creation date of the event."""

    LastChange = Column(DateTime, nullable=False, default=datetime.now())
    """The last change of the event."""


class Event(BaseModel):
    """Model to track events."""

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_pascal)

    id: int
    """The unique identifier of the event."""

    title: str
    """The title of the event."""

    description: Optional[str]
    """The description of the event."""

    time_frame: int
    """The time frame of the event."""

    expected_patricipant_count: int
    """The expected number of participants."""

    entry_fee_ct: int
    """The entry fee in cents."""

    expected_costs_ct: int
    """The expected costs in cents."""

    expected_cost_reasons: Optional[str]
    """The reasons for the expected costs."""

    is_studentic: Optional[bool] = False
    """Whether the event is a student initiative."""

    is_live_music_played: Optional[bool] = False
    """Whether live music is played at the event."""

    is_gema_required: Optional[bool] = False
    """Whether GEMA is required for the event."""

    organisation: Optional[int] = None
    """The organisation reference responsible for the event."""

    room_reservation: Optional[int] = None
    """The room reservation for the event."""

    item_reservation: Optional[int] = None
    """The item reservation refrence for the event."""

    poster_path: Optional[str]
    """The path to the poster image of the event."""

    promo_image_path: Optional[str]
    """The path to the promotional image of the event."""

    type: EventType
    """The type of the event."""

    visibility: EventVisibility
    """The visibility of the event."""

    status: EventStatus
    """The status of the event."""

    external_remarks: Optional[str]
    """The external remarks of the event."""

    internal_remarks: Optional[str]
    """The internal remarks of the event."""

    requirements: Optional[str]
    """The requirements of the event."""

    publication_date: datetime
    """The publication date of the event."""

    created_by: int
    """The user reference who created the event."""

    creation_date: datetime
    """The creation date of the event."""

    last_change: datetime
    """The last change of the event."""
