// Backend/src/models/addressemails.go
// Definition of the AddressEmails model that connects addresses and emails.

// Author: Valentin Haas, 2025
package models

import (
	"time"
)

// AddressEmails represents the model that connects addresses and emails in the database.
type AddressEmail struct {
	Address   Address
	AddressID uint      `gorm:"primaryKey"` // The address of the email with a primary key constraint.
	Email     Email     // Referenced Email Object
	EmailID   uint      `gorm:"primaryKey"` // The email of the address with a primary key constraint.
	CreatedAt time.Time // Time the model was created. Auto Populated by Gorm.
	UpdatedAt time.Time // Time the model was updated. Auto Populated by Gorm.
	DeletedAt time.Time // Time the model was deleted. Auto Populated by Gorm.
	IsPrimary bool      `gorm:"default:true;not null"` // Indicates whether the email is the primary one for the address.
}
