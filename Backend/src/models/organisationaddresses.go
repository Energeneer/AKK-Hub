// /Backend/src/models/organisationaddresses.go
// Definition of the OrganisationAddress model, connecting Organisations and Addresses

// Author: Valentin Haas, 2025
package models

import "time"

// OrganisationAddresses is a model to connect Organisations and Addresses.
type OrganisationAddresse struct {
	Organisation   Organisation // Referenced Organisation Object
	OrganisationID uint         `gorm:"primaryKey"` // Th unique identifier of the organisation.
	Address        Address      // Referenced Address Object
	AddressID      uint         `gorm:"primaryKey"` // The unique identifier of the address.
	CreatedAt      time.Time    // Time the model was created. Auto Populated by Gorm.
	UpdatedAt      time.Time    // Time the model was updated. Auto Populated by Gorm.
	DeletedAt      time.Time    // Time the model was deleted. Auto Populated by Gorm.
	IsPrimary      bool         `gorm:"not null;default:true"` // Indicates whether the address is the primary address for the organisation.
}
