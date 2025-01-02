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
	User       User       `gorm:"primaryKey"` // The unique identifier of the user.
	Site       LinkedSite `gorm:"primaryKey"` // The unique identifier of the linked site.
}
