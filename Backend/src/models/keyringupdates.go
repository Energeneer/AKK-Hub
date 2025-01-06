// Backend/src/models/keyringupdates.go
// Definition of the KeyRingUpdate model, tracking updates to key_rings

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// KeyRingUpdate tracks the updates of key_rings.
type KeyRingUpdate struct {
	gorm.Model             // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	KeyRing     KeyRing    // Referenced KeyRing Object
	KeyRingID   uint       `gorm:"not null"` // The key_ring that was updated (foreign key reference to KeyRings.Id).
	Type        UpdateType `gorm:"not null"` // The type of the update.
	Title       string     `gorm:"not null"` // The title of the update.
	UpdatedBy   User
	UpdatedByID uint    `gorm:"not null"` // The user who updated the group (foreign key reference to Users.Id).
	Text        *string // The text of the update, optional.
}
