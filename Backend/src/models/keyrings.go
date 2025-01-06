// Backend/src/models/keyrings.go
// Definition of the KeyRing model

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// KeyRing represents the key rings in the system.
type KeyRing struct {
	gorm.Model                     // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	Label             string       `gorm:"not null"`  // The label of the key ring.
	Description       *string      `gorm:"type:text"` // The description of the key ring, optional.
	ImagePath         *string      // The path to the image of the key ring, optional.
	DefaultLocation   RoomLocation // Referenced RoomLocation Object
	DefaultLocationID uint         `gorm:"not null"` // The default location of the key ring.
	CurrentLocation   RoomLocation // Referenced RoomLocation Object
	CurrentLocationID uint         `gorm:"not null"` // The current location of the key ring.
}
