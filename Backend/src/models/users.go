// Backend/src/models/users.go
// Definition of the User model

// Author: Valentin Haas, 2025
package models

import (
	"time"

	"gorm.io/gorm"
)

// User represents the user model for the database.
type User struct {
	gorm.Model                   // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	Nickname          string     // The nickname of the user.
	Username          *string    `gorm:"unique"` // The username of the user.
	PasswordHash      *string    // The hashed password of the user.
	OAuthToken        *string    // The OAuth token of the user when using OAuth authentication.
	WebAuthToken      *string    // The web authentication token of the user for web authentication.
	Title             *string    // The title of the user.
	FirstName         *string    // The first name of the user.
	MiddleNames       *string    // The middle names of the user.
	LastName          *string    // The last name of the user.
	Initials          *string    // The initials of the user.
	Birthdate         *time.Time // The birthdate of the user.
	PublicImagePath   *string    // The path to the public image of the user.
	InternalImagePath *string    // The path to the internal image of the user.
	Description       *string    // The description of the user the user can set.
	IsBlocked         bool       // The blocked status of the user.
	InternalRemark    *string    // The internal remark of the user.
}
