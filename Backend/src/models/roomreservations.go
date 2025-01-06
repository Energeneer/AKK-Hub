// Backend/src/models/roomreservations.go
// Definition of the RoomReservation model

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// RoomReservationStatus is an enum to track the status of the room reservation.
type RoomReservationStatus int

const (
	PENDING  RoomReservationStatus = iota // The room reservation is pending.
	ACCEPTED                              // The room reservation is accepted.
	DECLINED                              // The room reservation is declined.
)

// RoomReservations is a model for tracking room reservations.
type RoomReservation struct {
	gorm.Model                        // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	TimeFrame   TimeFrame             // Referenced TimeFrame Object
	TimeFrameID uint                  `gorm:"not null"` // The time frame of the room reservation.
	Room        Room                  // Referenced Room Object
	RoomID      uint                  `gorm:"not null"` // The room of the room reservation.
	CreatedBy   User                  // Referenced User Object
	CreatedByID uint                  `gorm:"not null"`          // The user who created the room reservation.
	Status      RoomReservationStatus `gorm:"type:int;not null"` // The status of the room reservation.
}
