// Backend/src/models/itemreservationupdates.go
// Definition of the ItemReservationUpdate model, tracking updates to item_reservations.

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// ItemReservationUpdates represents the updates of inventory item types.
type ItemReservationUpdate struct {
	gorm.Model                 // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	ItemReservation uint       `gorm:"not null;foreignKey:ItemReservationID"` // The item reservation that was updated (foreign key reference to ItemReservations.Id).
	Type            UpdateType `gorm:"not null"`                              // The type of the update.
	Title           string     `gorm:"not null"`                              // The title of the update.
	UpdatedBy       uint       `gorm:"not null;foreignKey:UserID"`            // The user who updated the group (foreign key reference to Users.Id).
	Text            *string    // The text of the update.
}
