// Backend/src/models/userorganisations.go
// Definition of the UserOrganisation model, connecting users and organisations

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// UserOrganisation defines the relationship between users and organisations.
type UserOrganisation struct {
	gorm.Model        // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	User         uint `gorm:"primaryKey;not null;foreignKey:UserID"`         // The user in the relationship (foreign key reference to User.ID).
	Organisation uint `gorm:"primaryKey;not null;foreignKey:OrganisationID"` // The organisation in the relationship (foreign key reference to Organisation.ID).
}
