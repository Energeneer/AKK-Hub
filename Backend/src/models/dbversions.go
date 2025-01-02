// Backend/src/models/dbversions.go
// Model to track the database version history

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// DBVersions model to track the database version history.
type DBVersion struct {
	gorm.Model              // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	DatabaseVersion int     `gorm:"primaryKey"`                 // The version of the database schema.
	ProductVersion  string  `gorm:"type:varchar(16); not null"` // The version of the product that was released with this database schema.
	Description     *string `gorm:"type:text; default:null"`    // A description of the changes made in this database schema.
}
