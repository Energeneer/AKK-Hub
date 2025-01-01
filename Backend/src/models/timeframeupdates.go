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
	TimeFrame  int        `gorm:"not null"` // The key affected by the update.
	Type       UpdateType `gorm:"not null"` // The type of the update.
	Title      string     `gorm:"not null"` // The title of the update.
	UpdatedBy  int        `gorm:"not null"` // The user who updated the time_frame.
	Text       *string    // The text of the update.
}
