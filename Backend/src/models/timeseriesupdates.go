// Backend/src/models/timeseriesupdates.go
// Definition of the TimeSeriesUpdate model, tracking updates to time_seriess

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// TimeSeriesUpdateType represents the available update types for a time series.
type TimeSeriesUpdateType string // Enum type placeholder

// TimeSeriesUpdate defines the TimeSeriesUpdate model for the database.
type TimeSeriesUpdate struct {
	gorm.Model            // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	TimeSeries uint       `gorm:"not null;foreignKey:TimeSeriesID"` // The time series that was updated (foreign key reference to TimeSeriess.Id).
	Type       UpdateType `gorm:"not null"`                         // The type of the update.
	Title      string     `gorm:"not null"`                         // The title of the update.
	UpdatedBy  uint       `gorm:"not null;foreignKey:UserID"`       // The user who updated the group (foreign key reference to Users.Id).
	Text       *string    `gorm:"type:text"`                        // The text of the update.
}
