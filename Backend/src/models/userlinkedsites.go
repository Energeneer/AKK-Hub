// Backend/src/models/userlinkedsites.go
// Definition of the UserLinkedSite model, connecting users and linked sites

// Author: Valentin Haas, 2025
package models

import "time"

// UserLinkedSite defines the relationship between users and linked sites.
type UserLinkedSite struct {
	User      User       // Referenced User Object
	UserID    uint       `gorm:"primaryKey"` // The user in the relationship (foreign key reference to User.ID).
	Site      LinkedSite // Referenced LinkedSite Object
	SiteID    uint       `gorm:"primaryKey"` // The linked site in the relationship (foreign key reference to LinkedSite.ID).
	CreatedAt time.Time  // Time the model was created. Auto Populated by Gorm.
	UpdatedAt time.Time  // Time the model was updated. Auto Populated by Gorm.
	DeletedAt time.Time  // Time the model was deleted. Auto Populated by Gorm.
}
