// Backend/src/models/usertelnumbers.go
// Definition of the UserTelNumber model, connecting users and telephone numbers

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// UserTelNumber represents the user-telephone number model for the database.
type UserTelNumber struct {
	gorm.Model      // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	User       uint `gorm:"primaryKey;not null;foreignKey:UserID"`      // The user in the relationship (foreign key reference to User.ID).
	TelNumber  uint `gorm:"primaryKey;not null;foreignKey:TelNumberID"` // The telephone number in the relationship (foreign key reference to TelNumber.ID).
	IsPrimary  bool // Whether the telephone number is the primary telephone number of the user.
}
