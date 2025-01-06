// Backend/src/models/lockupdates.go
// Definition of the LockUpdate model, tracking updates to locks

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// LockUpdates is a model to track the updates of locks.
type LockUpdate struct {
	gorm.Model         // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	Lock        Lock   // Referenced Lock Object
	LockID      uint   `gorm:"not null"` // The lock that was updated (foreign key reference to Locks.Id).
	Title       string `gorm:"not null"` // The title of the update.
	UpdatedBy   User   // Referenced User Object
	UpdatedByID uint   `gorm:"not null"`     // The user who updated the group (foreign key reference to Users.Id).
	Text        string `gorm:"default:null"` // The text of the update.
}
