// Backend/src/models/organisationtelnumbers.go
// Definition of the OrganisationTelNumber model, connecting organisations and telephone numbers

// Author: Valentin Haas, 2025
package models

import "time"

// OrganisationTelNumbers is a model representing the connection between organisations and telephone numbers.
type OrganisationTelNumber struct {
	Organisation   Organisation    // Referenced Organisation Object
	OrganisationID uint            `gorm:"primaryKey"` // The unique identifier of the organisation.
	TelNumber      TelephoneNumber // Refrenced TelephoneNumber Object
	TelNumberID    int             `gorm:"primaryKey"` // The unique identifier of the telephone number.
	CreatedAt      time.Time       // Time the model was created. Auto Populated by Gorm.
	UpdatedAt      time.Time       // Time the model was updated. Auto Populated by Gorm.
	DeletedAt      time.Time       // Time the model was deleted. Auto Populated by Gorm.
	IsPrimary      bool            `gorm:"default:false"` // Whether the telephone number is the primary telephone number of the organisation.
}
