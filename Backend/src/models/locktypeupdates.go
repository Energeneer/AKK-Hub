// Backend/src/models/locktypeupdates.go
// Definition of the LockTypeUpdate model, tracking updates to lock_types

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// LockTypeUpdates is a model to track the updates of lock_types.
type LockTypeUpdate struct {
	gorm.Model             // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	LockType    LockType   // Referenced LockType Object
	LockTypeID  uint       `gorm:"not null"` // The lock_type that was updated (foreign key reference to LockTypes.Id).
	Type        UpdateType `gorm:"not null"` // The type of the update.
	Title       string     `gorm:"not null"` // The title of the update.
	UpdatedBy   User       // Referenced User Object
	UpdatedByID uint       `gorm:"not null"`     // The user who updated the group (foreign key reference to Users.Id).
	Text        string     `gorm:"default:null"` // The text of the update.
}
