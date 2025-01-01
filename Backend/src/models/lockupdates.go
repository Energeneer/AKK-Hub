// Backend/src/models/lockupdates.go
// Definition of the LockUpdate model, tracking updates to locks

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// LockUpdates is a model to track the updates of locks.
type LockUpdate struct {
	gorm.Model        // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	Lock       int    `gorm:"not null"`     // The lock affected by the update.
	Title      string `gorm:"not null"`     // The title of the update.
	UpdatedBy  int    `gorm:"not null"`     // The user who updated the lock.
	Text       string `gorm:"default:null"` // The text of the update.
}
