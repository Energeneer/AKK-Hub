// Backend/src/models/organisationemails.go
// Definition of the OrganisationEmail model, connecting organisations and emails

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// OrganisationEmails is a model to connect organisations and emails.
type OrganisationEmail struct {
	gorm.Model                  // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	Organisation   Organisation // Referenced Organisation Object
	OrganisationID uint         `gorm:"primaryKey"` // The unique identifier of the organisation.
	Email          Email        // Referenced Email Object
	EmailID        uint         `gorm:"primaryKey"`             // The unique identifier of the email.
	IsPrimary      bool         `gorm:"not null;default:false"` // Whether the email is the primary email of the organisation.
}
