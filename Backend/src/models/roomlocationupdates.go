// Backend/src/models/roomlocationupdates.go
// Definition of the RoomLocationUpdate model, tracking updates to room_locations

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// RoomLocationUpdates is a model for tracking updates to room locations.
type RoomLocationUpdate struct {
	gorm.Model              // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	RoomLocation uint       `gorm:"not null;foreignKey:RoomLocationID"` // The room_location that was updated (foreign key reference to RoomLocations.Id).
	Type         UpdateType `gorm:"not null"`                           // The type of the update.
	Title        string     `gorm:"not null"`                           // The title of the update.
	UpdatedBy    uint       `gorm:"not null;foreignKey:UserID"`         // The user who updated the group (foreign key reference to Users.Id).
	Text         *string    // The text of the update.
}
