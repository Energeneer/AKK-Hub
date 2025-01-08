// Backend/src/models/timeframes.go
// Definition of the TimeFrame model

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
	"time"
)

// TimeFrames defines the TimeFrame model for the database.
type TimeFrame struct {
	gorm.Model              // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	StartTime    time.Time  `gorm:"not null"` // The start time of the time frame.
	EndTime      time.Time  `gorm:"not null"` // The end time of the time frame.
	TimeSeries   TimeSeries // Referenced TimeSeries Object
	TimeSeriesID *uint      `gorm:"default:null"` // A optional TimeSeries for repeating events (foreign key reference to TimeSeries.Id).
}
