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
	Key        uint       `gorm:"not null;foreignKey:KeyID"`  // The key that was updated (foreign key reference to Keys.Id).
	Type       UpdateType `gorm:"not null"`                   // The type of the update.
	Title      string     `gorm:"not null"`                   // The title of the update.
	UpdatedBy  uint       `gorm:"not null;foreignKey:UserID"` // The user who updated the group (foreign key reference to Users.Id).
	Text       *string    `gorm:"default:null"`               // The text of the update.
}
