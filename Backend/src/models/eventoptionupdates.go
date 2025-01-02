// Backend/src/models/eventoptionupdates.go
// Definition of the EventOptionUpdate model, tracking updates to EventOptions

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// EventOptionUpdatesModel to track the updates of EventOptions.
type EventOptionUpdate struct {
	gorm.Model             // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	EventOption uint       `gorm:"not null;foreignKey:EventOptionID"` // The EventOption that was updated (foreign key reference to EventOptions.Id).
	Type        UpdateType `gorm:"type:varchar(255);not null"`        // The type of the update.
	Title       string     `gorm:"type:varchar(255);not null"`        // The title of the update.
	UpdatedBy   uint       `gorm:"not null;foreignKey:UserID"`        // The user who updated the EventOption (foreign key reference to Users.Id).
	Text        *string    `gorm:"type:text;default:null"`            // The text of the update.
}
