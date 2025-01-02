// Backend/src/models/buildings.go
// Description: Buildings model for storing building data

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// Buildings definition of the Buildings model for the database.
type Building struct {
	gorm.Model         // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	Address    int     `gorm:"not null; foreignKey:AddressID"` // The address reference of the building.
	Name       string  `gorm:"not null"`                       // The name of the building.
	Nickname   *string `gorm:"default:null"`                   // The nickname of the building.
}
