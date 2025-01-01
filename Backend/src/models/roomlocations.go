// Backend/src/models/roomlocations.go
// Definition of locations within a room. May be recursive to allow for nested locations.

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// RoomLocations is a model for defining locations within a room.
type RoomLocation struct {
	gorm.Model           // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	Name         string  `gorm:"not null"` // The name of the location.
	Room         int     `gorm:"not null"` // The room in which the location is located.
	RoomLocation *int    // The parent location of the location.
	Description  *string // The description of the location.
	ImagePath    *string // The path to the image of the location.
}
