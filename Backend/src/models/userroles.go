// Backend/src/models/userroles.go
// Many to Many relationship between users and roles

// Author: Valentin Haas, 2025
package models

import "time"

// UserRole tracks the relationship between users and roles.
type UserRole struct {
	User      User      // Referenced User Object
	UserID    uint      `gorm:"primaryKey"` // The user in the relationship (foreign key reference to User.ID).
	Role      Role      // Referenced Role Object
	RoleID    uint      `gorm:"primaryKey"` // The role in the relationship (foreign key reference to Role.ID).
	CreatedAt time.Time // Time the model was created. Auto Populated by Gorm.
	UpdatedAt time.Time // Time the model was updated. Auto Populated by Gorm.
	DeletedAt time.Time // Time the model was deleted. Auto Populated by Gorm.
}
