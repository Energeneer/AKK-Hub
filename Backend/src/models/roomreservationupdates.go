// Backend/src/models/roomreservationupdates.go
// Definition of the RoomReservationUpdate model, tracking updates to room_reservations

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// RoomReservationUpdates is a model for tracking updates of room reservations.
type RoomReservationUpdate struct {
	gorm.Model                        // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	RoomReservation   RoomReservation // Referenced RoomReservation Object
	RoomReservationID uint            `gorm:"not null"`          // The room_reservation that was updated (foreign key reference to RoomReservations.Id).
	Type              UpdateType      `gorm:"type:int;not null"` // The type of the update.
	Title             string          `gorm:"not null"`          // The title of the update.
	UpdatedBy         User            // Referenced User Object
	UpdatedByID       uint            `gorm:"not null"` // The user who updated the group (foreign key reference to Users.Id).
	Text              *string         // The text of the update.
}
