// Backend/src/models/userorganisations.go
// Definition of the UserOrganisation model, connecting users and organisations

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// UserOrganisation defines the relationship between users and organisations.
type UserOrganisation struct {
	gorm.Model                // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	User         User         `gorm:"primaryKey"` // The unique identifier of the user.
	Organisation Organisation `gorm:"primaryKey"` // The unique identifier of the organisation.
}
