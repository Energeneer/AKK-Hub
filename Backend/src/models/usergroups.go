// Backend/src/models/usergroups.go
// Many to Many relationship between users and groups

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// UserGroup tracks the relationship between users and groups.
type UserGroup struct {
	gorm.Model       // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	User       User  // Referenced User Object
	UserID     uint  `gorm:"primaryKey;not null;foreignKey:UserID"` // The user in the relationship.
	Group      Group // Referenced Group Object
	GroupID    uint  `gorm:"primaryKey;not null;foreignKey:GroupID"` // The group in the relationship.
}
