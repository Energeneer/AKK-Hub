// /Backend/src/models/organisationaddresses.go
// Definition of the OrganisationAddress model, connecting Organisations and Addresses

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// OrganisationAddresses is a model to connect Organisations and Addresses.
type OrganisationAddresse struct {
	gorm.Model                  // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	Organisation   Organisation // Referenced Organisation Object
	OrganisationID uint         `gorm:"primaryKey"` // Th unique identifier of the organisation.
	Address        Address      // Referenced Address Object
	AddressID      uint         `gorm:"primaryKey"`            // The unique identifier of the address.
	IsPrimary      bool         `gorm:"not null;default:true"` // Indicates whether the address is the primary address for the organisation.
}
