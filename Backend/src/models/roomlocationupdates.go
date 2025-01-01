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
	RoomLocation int        `gorm:"not null"` // The room_location affected by the update.
	Type         UpdateType `gorm:"not null"` // The type of the update.
	Title        string     `gorm:"not null"` // The title of the update.
	UpdatedBy    int        `gorm:"not null"` // The user who updated the room_location.
	Text         *string    // The text of the update.
}
