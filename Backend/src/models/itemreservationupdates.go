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
	ItemReservation int        `gorm:"not null"` // The key affected by the update.
	Type            UpdateType `gorm:"not null"` // The type of the update.
	Title           string     `gorm:"not null"` // The title of the update.
	UpdatedBy       int        `gorm:"not null"` // The user who updated the inventory item type.
	Text            *string    // The text of the update.
}
