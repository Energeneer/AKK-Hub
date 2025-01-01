// Backend/src/models/building_updates.go
// Definition of the BuildingUpdate model, tracking updates to buildings

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// BuildingUpdate model to track the updates of buildings.
type BuildingUpdate struct {
	gorm.Model            // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	Building   int        `gorm:"not null"`                                 // The building affected by the update.
	Type       UpdateType `gorm:"not null"`                                 // The type of the update.
	Title      string     `gorm:"not null"`                                 // The title of the update.
	UpdatedBy  int        `gorm:"not null; foreignKey:User; references:ID"` // The user who updated the building.
	Text       *string    `gorm:"type:text; default:null"`                  // The text of the update.
}
