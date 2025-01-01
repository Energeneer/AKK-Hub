// Backend/src/models/organisationtelnumbers.go
// Definition of the OrganisationTelNumber model, connecting organisations and telephone numbers

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// OrganisationTelNumbers is a model representing the connection between organisations and telephone numbers.
type OrganisationTelNumber struct {
	gorm.Model          // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	OrganisationID int  `gorm:"primaryKey"`    // The unique identifier of the organisation.
	TelNumberID    int  `gorm:"primaryKey"`    // The unique identifier of the telephone number.
	IsPrimary      bool `gorm:"default:false"` // Whether the telephone number is the primary telephone number of the organisation.
}
