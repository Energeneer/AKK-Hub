// Backend/src/models/userorganisations.go
// Definition of the UserOrganisation model, connecting users and organisations

// Author: Valentin Haas, 2025
package models

import "time"

// UserOrganisation defines the relationship between users and organisations.
type UserOrganisation struct {
	User           User         // Referenced User Object
	UserID         uint         `gorm:"primaryKey"` // The user in the relationship (foreign key reference to User.ID).
	Organisation   Organisation // Referenced Organisation Object
	OrganisationID uint         `gorm:"primaryKey"` // The organisation in the relationship (foreign key reference to Organisation.ID).
	CreatedAt      time.Time    // Time the model was created. Auto Populated by Gorm.
	UpdatedAt      time.Time    // Time the model was updated. Auto Populated by Gorm.
	DeletedAt      time.Time    // Time the model was deleted. Auto Populated by Gorm.
}
