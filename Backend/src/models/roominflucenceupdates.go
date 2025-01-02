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
	RoomInflucence uint       `gorm:"not null;foreignKey:RoomInflucenceID"` // The room_influcence that was updated (foreign key reference to RoomInflucences.Id).
	Type           UpdateType `gorm:"not null"`                             // The type of the update.
	Title          string     `gorm:"not null"`                             // The title of the update.
	UpdatedBy      uint       `gorm:"not null;foreignKey:UserID"`           // The user who updated the group (foreign key reference to Users.Id).
	Text           string     `gorm:"default:null"`                         // The text of the update.
}
