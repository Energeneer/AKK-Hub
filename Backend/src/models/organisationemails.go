// Backend/src/models/organisationemails.go
// Definition of the OrganisationEmail model, connecting organisations and emails

// Author: Valentin Haas, 2025
package models

import "time"

// OrganisationEmails is a model to connect organisations and emails.
type OrganisationEmail struct {
	Organisation   Organisation // Referenced Organisation Object
	OrganisationID uint         `gorm:"primaryKey"` // The unique identifier of the organisation.
	Email          Email        // Referenced Email Object
	EmailID        uint         `gorm:"primaryKey"` // The unique identifier of the email.
	CreatedAt      time.Time    // Time the model was created. Auto Populated by Gorm.
	UpdatedAt      time.Time    // Time the model was updated. Auto Populated by Gorm.
	DeletedAt      time.Time    // Time the model was deleted. Auto Populated by Gorm.
	IsPrimary      bool         `gorm:"not null;default:false"` // Whether the email is the primary email of the organisation.
}
