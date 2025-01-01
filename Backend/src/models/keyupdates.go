// Backend/src/models/keyupdates.go
// Definition of the KeyUpdate model, tracking updates to keys

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// KeyUpdates defines the structure for tracking updates to keys.
type KeyUpdate struct {
	gorm.Model            // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	Key        int        `gorm:"not null"`     // The key affected by the update.
	Type       UpdateType `gorm:"not null"`     // The type of the update.
	Title      string     `gorm:"not null"`     // The title of the update.
	UpdatedBy  int        `gorm:"not null"`     // The user who updated the key.
	Text       *string    `gorm:"default:null"` // The text of the update.
}
