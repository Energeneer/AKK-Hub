// Backend/src/models/roominflucenceupdates.go
// Definition of the RoomInflucenceUpdate model, tracking updates to room_influcences

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// RoomInflucenceUpdates is a model to track the updates of room_influcences.
type RoomInflucenceUpdate struct {
	gorm.Model                // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	RoomInflucence int        `gorm:"not null"`     // The room_influcence affected by the update.
	Type           UpdateType `gorm:"not null"`     // The type of the update.
	Title          string     `gorm:"not null"`     // The title of the update.
	UpdatedBy      int        `gorm:"not null"`     // The user who updated the room_influcence.
	Text           string     `gorm:"default:null"` // The text of the update.
}
