// Backend/src/models/roleupdates.go
// Definition of the RoleUpdate model, tracking updates to roles

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// RoleUpdates is a model to track the updates of roles.
type RoleUpdate struct {
	gorm.Model            // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	Role       int        `gorm:"not null"`                   // The role affected by the update.
	Type       UpdateType `gorm:"not null"`                   // The type of the update.
	Title      string     `gorm:"type:varchar(255);not null"` // The title of the update.
	UpdatedBy  int        `gorm:"not null"`                   // The user who updated the role.
	Text       *string    `gorm:"type:text"`                  // The text of the update.
}
