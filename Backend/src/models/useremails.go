// Backend/src/models/useremails.go
// Definition of the UserEmail model, connecting users and emails

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// UserEmail defines the UserEmail model for the database.
type UserEmail struct {
	gorm.Model      // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	User       int  `gorm:"primaryKey"`             // The unique identifier of the user.
	Email      int  `gorm:"primaryKey"`             // The unique identifier of the email.
	IsPrimary  bool `gorm:"not null;default:false"` // Whether the email is the primary email of the user.
}
