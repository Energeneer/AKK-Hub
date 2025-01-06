// Backend/src/models/eventoptionupdates.go
// Definition of the EventOptionUpdate model, tracking updates to EventOptions

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// EventOptionUpdatesModel to track the updates of EventOptions.
type EventOptionUpdate struct {
	gorm.Model    // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	EventOption   EventOption
	EventOptionID uint       `gorm:"not null"` // The EventOption that was updated (foreign key reference to EventOptions.Id).
	Type          UpdateType `gorm:"not null"` // The type of the update.
	Title         string     `gorm:"not null"` // The title of the update.
	UpdatedBy     User       // Referenced User Object
	UpdatedByID   uint       `gorm:"not null"`               // The user who updated the EventOption (foreign key reference to Users.Id).
	Text          *string    `gorm:"type:text;default:null"` // The text of the update.
}
