// Backend/src/models/useremails.go
// Definition of the UserEmail model, connecting users and emails

// Author: Valentin Haas, 2025
package models

import "time"

// UserEmail defines the UserEmail model for the database.
type UserEmail struct {
	User      User      // Referenced User Object
	UserID    int       `gorm:"primaryKey"` // The unique identifier of the user.
	Email     Email     // Referenced Email Object
	EmailID   int       `gorm:"primaryKey"` // The unique identifier of the email.
	CreatedAt time.Time // Time the model was created. Auto Populated by Gorm.
	UpdatedAt time.Time // Time the model was updated. Auto Populated by Gorm.
	DeletedAt time.Time // Time the model was deleted. Auto Populated by Gorm.
	IsPrimary bool      `gorm:"not null;default:false"` // Whether the email is the primary email of the user.
}
