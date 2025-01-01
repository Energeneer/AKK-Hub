// Backend/src/models/usertelnumbers.go
// Definition of the UserTelNumber model, connecting users and telephone numbers

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// UserTelNumber represents the user-telephone number model for the database.
type UserTelNumber struct {
	gorm.Model                 // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	User       User            `gorm:"primaryKey"` // The unique identifier of the user.
	TelNumber  TelephoneNumber `gorm:"primaryKey"` // The unique identifier of the telephone number.
	IsPrimary  bool            // Whether the telephone number is the primary telephone number of the user.
}
