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
	User       uint       // The user affected by the update.
	Type       UpdateType // The type of the update.
	Title      string     // The title of the update.
	UpdatedBy  uint       // The user who updated the user.
	Text       *string    // The text of the update.
}
