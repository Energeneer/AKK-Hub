// Backend/src/models/timeseries.go
// Definition of the TimeSeries model

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// TimeSeries defines the TimeSeries model for the database.
type TimeSeries struct {
	gorm.Model        // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	Rule       string `gorm:"not null"` // The rule of the time series.
}
