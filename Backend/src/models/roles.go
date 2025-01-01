// Backend/src/models/roles.go
// Definition of the Role model, tracking roles of users

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// Roles is a model to track the roles of users.
type Role struct {
	gorm.Model          // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	Name        string  `gorm:"type:varchar(255);not null"` // The name of the role.
	Description *string `gorm:"type:text"`                  // The description of the role.
}
