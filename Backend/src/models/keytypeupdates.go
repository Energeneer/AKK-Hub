// Backend/src/models/keytypeupdates.go
// Definition of the KeyTypeUpdate model, tracking updates to key_types

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// KeyTypeUpdates defines the structure for tracking updates to key_types.
type KeyTypeUpdate struct {
	gorm.Model             // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	KeyType     KeyType    // Referenced KeyType Object
	KeyTypeID   uint       `gorm:"not null"` // The key_type that was updated (foreign key reference to KeyTypes.Id).
	Type        UpdateType `gorm:"not null"` // The type of the update.
	Title       string     `gorm:"not null"` // The title of the update.
	UpdatedBy   User       // Referenced User Object
	UpdatedByID uint       `gorm:"not null"`     // The user who updated the group (foreign key reference to Users.Id).
	Text        *string    `gorm:"default:null"` // The text of the update.
}
