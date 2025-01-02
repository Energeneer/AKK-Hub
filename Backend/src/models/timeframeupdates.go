// Backend/src/models/timeframeupdates.go
// Definition of the TimeFrameUpdate model, tracking updates to time_frames

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// TimeFrameUpdates defines the TimeFrameUpdate model for the database.
type TimeFrameUpdate struct {
	gorm.Model            // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	TimeFrame  uint       `gorm:"not null;foreignKey:TimeFrameID"` // The time frame that was updated (foreign key reference to TimeFrames.Id).
	Type       UpdateType `gorm:"not null"`                        // The type of the update.
	Title      string     `gorm:"not null"`                        // The title of the update.
	UpdatedBy  uint       `gorm:"not null;foreignKey:UserID"`      // The user who updated the group (foreign key reference to Users.Id).
	Text       *string    // The text of the update.
}
