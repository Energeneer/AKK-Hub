// Backend/src/models/groupupdates.go
// Definition of the GroupUpdate model, tracking updates to Groups

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// GroupUpdates represents the model to track the updates of Groups.
type GroupUpdate struct {
	gorm.Model            // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	Group      int        `gorm:"not null"` // The Group affected by the update.
	Type       UpdateType `gorm:"not null"` // The type of the update.
	Title      string     `gorm:"not null"` // The title of the update.
	UpdatedBy  int        `gorm:"not null"` // The user who updated the Group.
	Text       *string    // The text of the update.
}
