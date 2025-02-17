// Backend/src/models/usergroups.go
// Many to Many relationship between users and groups

// Author: Valentin Haas, 2025
package models

import "time"

// UserGroup tracks the relationship between users and groups.
type UserGroup struct {
	User      User      // Referenced User Object
	UserID    uint      `gorm:"primaryKey;not null;foreignKey:UserID"` // The user in the relationship.
	Group     Group     // Referenced Group Object
	GroupID   uint      `gorm:"primaryKey;not null;foreignKey:GroupID"` // The group in the relationship.
	CreatedAt time.Time // Time the model was created. Auto Populated by Gorm.
	UpdatedAt time.Time // Time the model was updated. Auto Populated by Gorm.
	DeletedAt time.Time // Time the model was deleted. Auto Populated by Gorm.
}
