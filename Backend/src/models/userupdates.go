// Backend/src/models/userupdates.go
// Definition of the UserUpdate model, tracking updates to users

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// UserUpdate represents the user update model for the database.
type UserUpdate struct {
	gorm.Model            // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	User       uint       `gorm:"not null;foreignKey:UserID"` // The user that was updated (foreign key reference to Users.Id).
	Type       UpdateType // The type of the update.
	Title      string     // The title of the update.
	UpdatedBy  uint       `gorm:"not null;foreignKey:UserID"` // The user who updated the group (foreign key reference to Users.Id).
	Text       *string    // The text of the update.
}
