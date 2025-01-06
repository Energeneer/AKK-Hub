// /Backend/src/models/useraddresses.go
// Definition of the UserAddress model, connecting Users and Addresses

// Author: Valentin Haas, 2025
package models

import "time"

// UserAddress defines the UserAddress model for the database.
type UserAddress struct {
	User      User      // Referenced User Object
	UserID    int       `gorm:"primaryKey"` // The unique identifier of the user.
	Address   Address   // Referenced Address Object
	AddressID int       `gorm:"primaryKey"` // The unique identifier of the address.
	CreatedAt time.Time // Time the model was created. Auto Populated by Gorm.
	UpdatedAt time.Time // Time the model was updated. Auto Populated by Gorm.
	DeletedAt time.Time // Time the model was deleted. Auto Populated by Gorm.
	IsPrimary bool      `gorm:"not null;default:true"` // Indicates whether the address is the primary address for the user.
}
