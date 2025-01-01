// Backend/src/models/roomreservationupdates.go
// Definition of the RoomReservationUpdate model, tracking updates to room_reservations

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// RoomReservationUpdates is a model for tracking updates of room reservations.
type RoomReservationUpdate struct {
	gorm.Model                 // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	RoomReservation int        `gorm:"not null"`          // The room_reservation affected by the update.
	Type            UpdateType `gorm:"type:int;not null"` // The type of the update.
	Title           string     `gorm:"not null"`          // The title of the update.
	UpdatedBy       int        `gorm:"not null"`          // The user who updated the room_reservation.
	Text            *string    // The text of the update.
}
