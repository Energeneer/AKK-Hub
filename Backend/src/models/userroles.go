// Backend/src/models/userroles.go
// Many to Many relationship between users and roles

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// UserRole tracks the relationship between users and roles.
type UserRole struct {
	gorm.Model      // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	User       User `gorm:"primaryKey"` // The user in the relationship.
	Role       Role `gorm:"primaryKey"` // The role in the relationship.
}
