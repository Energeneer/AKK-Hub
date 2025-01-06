// Backend/src/models/roleupdates.go
// Definition of the RoleUpdate model, tracking updates to roles

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// RoleUpdates is a model to track the updates of roles.
type RoleUpdate struct {
	gorm.Model             // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	Role        Role       // Referenced Role Object
	RoleID      uint       `gorm:"not null;foreignKey:RoleID"` // The role that was updated (foreign key reference to Roles.Id).
	Type        UpdateType `gorm:"not null"`                   // The type of the update.
	Title       string     `gorm:"type:varchar(255);not null"` // The title of the update.
	UpdatedBy   User       // Referenced User Object
	UpdatedByID uint       `gorm:"not null;foreignKey:UserID"` // The user who updated the group (foreign key reference to Users.Id).
	Text        *string    `gorm:"type:text"`                  // The text of the update.
}
