// Backend/src/models/eventupdates.go
// Definition of the EventUpdate model, tracking updates to Events

// Author: Valentin Haas, 2025

package models

import (
	"gorm.io/gorm"
)

// EventUpdate models the tracking of updates to Events.
type EventUpdate struct {
	gorm.Model            // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	Event      int        `gorm:"column:Event;not null"`                    // The event affected by the update.
	Type       UpdateType `gorm:"not null"`                                 // The type of the update.
	Title      string     `gorm:"not null"`                                 // The title of the update.
	UpdatedBy  int        `gorm:"not null; foreignKey:User; references:ID"` // The user who updated the building.
	Text       *string    `gorm:"type:text; default:null"`                  // The text of the update.
}
