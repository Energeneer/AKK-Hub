// Backend/src/models/keyringupdates.go
// Definition of the KeyRingUpdate model, tracking updates to key_rings

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// KeyRingUpdate tracks the updates of key_rings.
type KeyRingUpdate struct {
	gorm.Model            // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	KeyRing    uint       `gorm:"not null"` // The key affected by the update.
	Type       UpdateType `gorm:"not null"` // The type of the update.
	Title      string     `gorm:"not null"` // The title of the update.
	UpdatedBy  uint       `gorm:"not null"` // The user who updated the key_ring.
	Text       *string    // The text of the update, optional.
}
