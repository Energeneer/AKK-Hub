// Backend/src/models/organisationlinkedsites.go
// Definition of the OrganisationLinkedSite model, connecting Organisations and linked sites

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// OrganisationLinkedSites is a model to connect Organisations and linked sites.
type OrganisationLinkedSite struct {
	gorm.Model                  // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	Organisation   Organisation // Referenced Organisation Object
	OrganisationID uint         `gorm:"primaryKey"` // The unique identifier of the Organisation.
	Site           LinkedSite   // Referenced LinkedSite Object
	SiteID         uint         `gorm:"primaryKey"` // The unique identifier of the linked site.
}
