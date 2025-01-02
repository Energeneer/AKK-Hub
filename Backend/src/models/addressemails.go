// Backend/src/models/addressemails.go
// Definition of the AddressEmails model that connects addresses and emails.

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// AddressEmails represents the model that connects addresses and emails in the database.
type AddressEmail struct {
	gorm.Model // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields

	Address   uint `gorm:"primaryKey;not null;foreignKey:AddressID"` // The address of the email with a primary key constraint.
	Email     uint `gorm:"primaryKey;not null;foreignKey:EmailID"`   // The email of the address with a primary key constraint.
	IsPrimary bool `gorm:"default:true;not null"`                    // Indicates whether the email is the primary one for the address.
}
