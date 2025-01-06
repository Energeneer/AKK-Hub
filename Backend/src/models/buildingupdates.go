// Backend/src/models/building_updates.go
// Definition of the BuildingUpdate model, tracking updates to buildings

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// BuildingUpdate model to track the updates of buildings.
type BuildingUpdate struct {
	gorm.Model  // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	Building    Building
	BuildingID  uint       `gorm:"not null"` // The building that was updated (foreign key reference to Buildings.Id).
	Type        UpdateType `gorm:"not null"` // The type of the update.
	Title       string     `gorm:"not null"` // The title of the update.
	UpdatedBy   User       // Referenced User Object
	UpdatedByID uint       `gorm:"not null"`                // The user who updated the group (foreign key reference to Users.Id).
	Text        *string    `gorm:"type:text; default:null"` // The text of the update.
}
