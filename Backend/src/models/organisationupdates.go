// Backend/src/models/organisationupdates.go
// Definition of the OrganisationUpdate model, tracking updates to organisations

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// OrganisationUpdates is a model to track the updates of organisations.
type OrganisationUpdate struct {
	gorm.Model                // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	OrganisationID uint       `gorm:"not null;foreignKey:OrganisationID"` // The organisation that was updated (foreign key reference to Organisations.Id).
	Type           UpdateType `gorm:"type:enum;not null"`                 // The type of the update.
	Title          string     `gorm:"not null"`                           // The title of the update.
	UpdatedBy      uint       `gorm:"not null;foreignKey:UserID"`         // The user who updated the group (foreign key reference to Users.Id).
	Text           *string    // The text of the update.
}
