// Backend/src/models/events.go
// Definition of the Event model, tracking events

// Author: Valentin Haas, 2025
package models

import (
	"time"

	"gorm.io/gorm"
)

// Enumeration types for event properties
type EventType int

const (
	OtherEventType EventType = iota
	Meeting
	Workshop
)

type EventVisibility int

const (
	Public EventVisibility = iota
	Private
	Internal
)

type EventStatus int

const (
	Draft EventStatus = iota
	Published
	Cancelled
	Deleted
)

// Events represents the model to track events.
type Event struct {
	gorm.Model                               // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	Title                    string          `gorm:"not null"`                              // The title of the event.
	Description              *string         `gorm:"default:null"`                          // The description of the event.
	TimeFrame                uint            `gorm:"not null;foreignKey:TimeFrameID"`       // The time frame of the event.
	ExpectedParticipantCount int             `gorm:"not null"`                              // The expected number of participants.
	EntryFeeCt               int             `gorm:"not null;default:0"`                    // The entry fee in cents.
	ExpectedCostsCt          int             `gorm:"not null;default:0"`                    // The expected costs in cents.
	ExpectedCostReasons      *string         `gorm:"default:null"`                          // The reasons for the expected costs.
	IsStudentic              bool            `gorm:"not null;default:false"`                // Whether the event is a Studentic event.
	IsLiveMusicPlayed        bool            `gorm:"not null;default:false"`                // Whether live music is played.
	IsGemaRequired           bool            `gorm:"not null;default:false"`                // Whether GEMA is required.
	Organisation             uint            `gorm:"not null;foreignKey:OrganisationID"`    // The organisation hosting the event (foreign key reference to Organisations.Id).
	RoomReservation          uint            `gorm:"not null;foreignKey:RoomReservationID"` // The room reservation for the event (foreign key reference to RoomReservations.Id).
	ItemReservation          uint            `gorm:"not null;foreignKey:ItemReservationID"` // The item reservation for the event (foreign key reference to ItemReservations.Id).
	PosterPath               *string         `gorm:"default:null"`                          // The path to the poster image.
	PromoImagePath           *string         `gorm:"default:null"`                          // The path to the promo image.
	Type                     EventType       `gorm:"not null"`                              // The type of the event.
	Visibility               EventVisibility `gorm:"not null"`                              // The visibility of the event.
	Status                   EventStatus     `gorm:"not null"`                              // The status of the event.
	ExternalRemarks          *string         `gorm:"default:null"`                          // Remarks visible to the public.
	InternalRemarks          *string         `gorm:"default:null"`                          // Remarks visible to the internal team only.
	Requirements             *string         `gorm:"default:null"`                          // Requirements for the event to happen.
	PublicationDate          time.Time       `gorm:"not null"`                              // The date the event was/will be published.
	CreatedBy                uint            `gorm:"not null;foreignKey:UserID"`            // The user who created the event (foreign key reference to Users.Id).
}
