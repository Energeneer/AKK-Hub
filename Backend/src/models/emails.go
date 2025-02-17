// Backend/src/models/emails.go
// Definition of the Email model

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// Emails definition of the Email model for the database.
type Email struct {
	gorm.Model        // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	Address    string `gorm:"not null"` // The address of the email.
	Label      string `gorm:"not null"` // The label of the email.
}
