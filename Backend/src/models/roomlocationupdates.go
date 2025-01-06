// Backend/src/models/roomlocationupdates.go
// Definition of the RoomLocationUpdate model, tracking updates to room_locations

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// RoomLocationUpdates is a model for tracking updates to room locations.
type RoomLocationUpdate struct {
	gorm.Model                  // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	RoomLocation   RoomLocation // Referenced RoomLocation Object
	RoomLocationID uint         `gorm:"not null"` // The room_location that was updated (foreign key reference to RoomLocations.Id).
	Type           UpdateType   `gorm:"not null"` // The type of the update.
	Title          string       `gorm:"not null"` // The title of the update.
	UpdatedBy      User         // Referenced User Object
	UpdatedByID    uint         `gorm:"not null"` // The user who updated the group (foreign key reference to Users.Id).
	Text           *string      // The text of the update.
}
