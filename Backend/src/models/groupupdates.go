// Backend/src/models/groupupdates.go
// Definition of the GroupUpdate model, tracking updates to Groups

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// GroupUpdates represents the model to track the updates of Groups.
type GroupUpdate struct {
	gorm.Model             // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	Group       Group      // Referenced Group Object
	GroupID     uint       `gorm:"not null;foreignKey:GroupID"` // The group that was updated (foreign key reference to Groups.Id).
	Type        UpdateType `gorm:"not null"`                    // The type of the update.
	Title       string     `gorm:"not null"`                    // The title of the update.
	UpdatedBy   User
	UpdatedByID uint    `gorm:"not null;foreignKey:UserID"` // The user who updated the group (foreign key reference to Users.Id).
	Text        *string // The text of the update.
}
