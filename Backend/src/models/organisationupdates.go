// Backend/src/models/organisationupdates.go
// Definition of the OrganisationUpdate model, tracking updates to organisations

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// OrganisationUpdates is a model to track the updates of organisations.
type OrganisationUpdate struct {
	gorm.Model                  // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	Organisation   Organisation // Referenced Organisation Object
	OrganisationID uint         `gorm:"not null"`           // The organisation that was updated (foreign key reference to Organisations.Id).
	Type           UpdateType   `gorm:"type:enum;not null"` // The type of the update.
	Title          string       `gorm:"not null"`           // The title of the update.
	UpdatedBy      User         // Referenced User Object
	UpdatedByID    uint         `gorm:"not null"` // The user who updated the group (foreign key reference to Users.Id).
	Text           *string      // The text of the update.
}
