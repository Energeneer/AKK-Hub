// Backend/src/models/organisationlinkedsites.go
// Definition of the OrganisationLinkedSite model, connecting Organisations and linked sites

// Author: Valentin Haas, 2025
package models

import "time"

// OrganisationLinkedSites is a model to connect Organisations and linked sites.
type OrganisationLinkedSite struct {
	Organisation   Organisation // Referenced Organisation Object
	OrganisationID uint         `gorm:"primaryKey"` // The unique identifier of the Organisation.
	Site           LinkedSite   // Referenced LinkedSite Object
	SiteID         uint         `gorm:"primaryKey"` // The unique identifier of the linked site.
	CreatedAt      time.Time    // Time the model was created. Auto Populated by Gorm.
	UpdatedAt      time.Time    // Time the model was updated. Auto Populated by Gorm.
	DeletedAt      time.Time    // Time the model was deleted. Auto Populated by Gorm.
}
