// Backend/src/models/keytypeupdates.go
// Definition of the KeyTypeUpdate model, tracking updates to key_types

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// KeyTypeUpdates defines the structure for tracking updates to key_types.
type KeyTypeUpdate struct {
	gorm.Model            // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	KeyType    int        `gorm:"not null"`     // The key_type affected by the update.
	Type       UpdateType `gorm:"not null"`     // The type of the update.
	Title      string     `gorm:"not null"`     // The title of the update.
	UpdatedBy  int        `gorm:"not null"`     // The user who updated the key_type.
	Text       *string    `gorm:"default:null"` // The text of the update.
}
