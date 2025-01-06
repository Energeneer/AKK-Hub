// Backend/src/models/userlinkedsites.go
// Definition of the UserLinkedSite model, connecting users and linked sites

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// UserLinkedSite defines the relationship between users and linked sites.
type UserLinkedSite struct {
	gorm.Model            // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	User       User       // Referenced User Object
	UserID     uint       `gorm:"primaryKey"` // The user in the relationship (foreign key reference to User.ID).
	Site       LinkedSite // Referenced LinkedSite Object
	SiteID     uint       `gorm:"primaryKey"` // The linked site in the relationship (foreign key reference to LinkedSite.ID).
}
