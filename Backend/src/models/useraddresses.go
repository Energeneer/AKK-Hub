// /Backend/src/models/useraddresses.go
// Definition of the UserAddress model, connecting Users and Addresses

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// UserAddress defines the UserAddress model for the database.
type UserAddress struct {
	User      int  `gorm:"primaryKey"`            // The unique identifier of the user.
	Address   int  `gorm:"primaryKey"`            // The unique identifier of the address.
	IsPrimary bool `gorm:"not null;default:true"` // Indicates whether the address is the primary address for the user.
}
