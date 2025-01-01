// Backend/src/models/events.go
// Definition of the Event model, tracking events

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
	"time"
)

// Enumeration types for event properties
type EventType int

const (
	Other EventType = iota
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
	Title                    string          `gorm:"not null"`
	Description              *string         `gorm:"default:null"`
	TimeFrame                int             `gorm:"not null"`
	ExpectedParticipantCount int             `gorm:"not null"`
	EntryFeeCt               int             `gorm:"not null;default:0"`
	ExpectedCostsCt          int             `gorm:"not null;default:0"`
	ExpectedCostReasons      *string         `gorm:"default:null"`
	IsStudentic              bool            `gorm:"not null;default:false"`
	IsLiveMusicPlayed        bool            `gorm:"not null;default:false"`
	IsGemaRequired           bool            `gorm:"not null;default:false"`
	Organisation             int             `gorm:"not null"`
	RoomReservation          int             `gorm:"not null"`
	ItemReservation          int             `gorm:"not null"`
	PosterPath               *string         `gorm:"default:null"`
	PromoImagePath           *string         `gorm:"default:null"`
	Type                     EventType       `gorm:"not null"`
	Visibility               EventVisibility `gorm:"not null"`
	Status                   EventStatus     `gorm:"not null"`
	ExternalRemarks          *string         `gorm:"default:null"`
	InternalRemarks          *string         `gorm:"default:null"`
	Requirements             *string         `gorm:"default:null"`
	PublicationDate          time.Time       `gorm:"not null"`
	CreatedBy                int             `gorm:"not null"`
}
