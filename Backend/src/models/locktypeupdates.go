// Backend/src/models/locktypeupdates.go
// Definition of the LockTypeUpdate model, tracking updates to lock_types

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// LockTypeUpdates is a model to track the updates of lock_types.
type LockTypeUpdate struct {
	gorm.Model            // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	LockType   int        `gorm:"not null"`     // The lock_type affected by the update.
	Type       UpdateType `gorm:"not null"`     // The type of the update.
	Title      string     `gorm:"not null"`     // The title of the update.
	UpdatedBy  int        `gorm:"not null"`     // The user who updated the lock_type.
	Text       string     `gorm:"default:null"` // The text of the update.
}
