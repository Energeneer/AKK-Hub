// Backend/src/models/itemreservations.go
// Definition of the ItemReservation model, tracking reservations of items (in events).

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// ItemReservationStatus represents the status of an item reservation.
type ItemReservationStatus int

const (
	OPEN ItemReservationStatus = iota
	HANDED_OUT
	RETURNED
	CANCELLED
)

// ItemReservationUnits represents the units of an item reservation.
type ItemReservationUnits int

const (
	Pieces ItemReservationUnits = iota
	Boxes
	Pallets
	Kg
	Liters
)

// ItemReservations represents the item reservations model.
type ItemReservation struct {
	gorm.Model                             // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	TimeFrame        int                   `gorm:"not null"` // The time frame of the reservation.
	ItemType         int                   `gorm:"not null"` // The type of the item to reserve.
	Unit             ItemReservationUnits  `gorm:"not null"` // The unit of the reservation.
	AmountHandedOut  int                   // The amount of the item that has been handed out.
	HandedOutBy      *int                  // The user who handed out the item.
	AmountReturned   *int                  `gorm:"default:0"` // The amount of the item that has been returned.
	ReturnAcceptedBy *int                  // The user who accepted the return of the item.
	CreatedBy        int                   `gorm:"not null"` // The user who created the reservation.
	Status           ItemReservationStatus `gorm:"not null"` // The status of the reservation.
}
