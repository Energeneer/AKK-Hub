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
	OrganisationID int        `gorm:"not null"`           // The organisation affected by the update.
	Type           UpdateType `gorm:"type:enum;not null"` // The type of the update.
	Title          string     `gorm:"not null"`           // The title of the update.
	UpdatedBy      int        `gorm:"not null"`           // The user who updated the organisation.
	Text           *string    // The text of the update.
}
