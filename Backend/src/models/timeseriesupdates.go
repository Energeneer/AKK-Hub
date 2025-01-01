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
	TimeSeries int        `gorm:"not null"`  // The key affected by the update.
	Type       UpdateType `gorm:"not null"`  // The type of the update.
	Title      string     `gorm:"not null"`  // The title of the update.
	UpdatedBy  int        `gorm:"not null"`  // The user who updated the time_series.
	Text       *string    `gorm:"type:text"` // The text of the update.
}
