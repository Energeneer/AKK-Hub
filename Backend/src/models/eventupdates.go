// Backend/src/models/eventupdates.go
// Definition of the EventUpdate model, tracking updates to Events

// Author: Valentin Haas, 2025

package models

import (
	"gorm.io/gorm"
)

// EventUpdate models the tracking of updates to Events.
type EventUpdate struct {
	gorm.Model             // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	Event       Event      // Referenced Event Object
	EventID     uint       `gorm:"not null"` // The event that was updated (foreign key reference to Events.Id).
	Type        UpdateType `gorm:"not null"` // The type of the update.
	Title       string     `gorm:"not null"` // The title of the update.
	UpdatedBy   User       // Referenced User Object
	UpdatedByID uint       `gorm:"not null"`                // The user who updated the building (foreign key reference to Users.Id).
	Text        *string    `gorm:"type:text; default:null"` // The text of the update.
}
