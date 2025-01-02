// Backend/src/models/participantupdates.go
// Definition of the ParticipantUpdate model, tracking updates to participants

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// ParticipantUpdates is a model to track the updates of participants.
type ParticipantUpdate struct {
	gorm.Model             // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	Participant uint       `gorm:"not null;foreignKey:ParticipantID"` // The participant that was updated (foreign key reference to Participants.Id).
	Type        UpdateType `gorm:"type:int;not null"`                 // The type of the update.
	Title       string     `gorm:"type:varchar(255);not null"`        // The title of the update.
	UpdatedBy   uint       `gorm:"not null;foreignKey:UserID"`        // The user who updated the group (foreign key reference to Users.Id).
	Text        *string    `gorm:"type:text"`                         // The text of the update.
}
