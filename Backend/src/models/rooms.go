// Backend/src/models/rooms.go
// Definition of the Room model

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// Rooms defines the Room model for the database.
type Room struct {
	gorm.Model           // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	Building    Building // Referenced Building Object
	BuildingID  uint     `gorm:"not null"` // The building reference of the room.
	Name        string   `gorm:"not null"` // The name of the room.
	Description *string  // The description of the room.
	RoomNumber  *string  // The room number of the room.
	CanBeBooked bool     `gorm:"default:false"` // Whether the room can be booked.
	SizeSqm     *float64 // The size of the room in square meters.
	CapacityPpl *int     // The capacity of the room in people.
}
