// Backend/src/models/linkedsites.go
// Definition of the LinkedSite model to represent external websites of entities

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// LinkedSites defines the structure for representing external websites.
type LinkedSite struct {
	gorm.Model         // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	Name       string  `gorm:"not null"` // The name of the linked site.
	Link       string  `gorm:"not null"` // The link to the linked site.
	IconPath   *string // The path to the icon of the linked site.
}
