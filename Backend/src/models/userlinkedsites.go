// Backend/src/models/userlinkedsites.go
// Definition of the UserLinkedSite model, connecting users and linked sites

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// UserLinkedSite defines the relationship between users and linked sites.
type UserLinkedSite struct {
	gorm.Model      // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	User       uint `gorm:"primaryKey;not null;foreignKey:UserID"` // The user in the relationship (foreign key reference to User.ID).
	Site       uint `gorm:"primaryKey;not null;foreignKey:SiteID"` // The linked site in the relationship (foreign key reference to LinkedSite.ID).
}
