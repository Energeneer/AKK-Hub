// Backend/src/models/addresses.go
// Definition of the Address model

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// Addresses represents the model for storing address information in the database.
type Address struct {
	gorm.Model // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields

	StreetName   string  `gorm:"not null"`     // The name of the street of the address.
	HouseNumber  string  `gorm:"not null"`     // The house number of the address.
	AddressLine2 *string `gorm:"default:null"` // The second line of the address.
	ZipCode      string  `gorm:"not null"`     // The ZIP code of the address.
	City         string  `gorm:"not null"`     // The city of the address.
	Country      string  `gorm:"not null"`     // The country of the address.
	Notes        *string `gorm:"default:null"` // Additional notes for the address.
}
