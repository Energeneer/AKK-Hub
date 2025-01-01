// Backend/src/models/groups.go
// Definition of the Group model, tracking groups of users

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// Groups represents the model to track the groups of users.
type Group struct {
	gorm.Model          // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	Name        string  `gorm:"not null"` // The name of the group.
	Description *string // The description of the group.
}
