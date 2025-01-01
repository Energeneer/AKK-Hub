// Backend/src/models/roomupdates.go
// Definition of the RoomUpdate model, tracking updates to rooms

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// RoomUpdates defines the RoomUpdate model for the database.
type RoomUpdate struct {
	gorm.Model            // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	Room       int        `gorm:"not null"` // The room affected by the update.
	Type       UpdateType `gorm:"not null"` // The type of the update.
	Title      string     `gorm:"not null"` // The title of the update.
	UpdatedBy  int        `gorm:"not null"` // The user who updated the room.
	Text       *string    // The text of the update.
}
