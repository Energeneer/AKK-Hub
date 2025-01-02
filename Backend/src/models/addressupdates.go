// Backend/src/models/addressupdates.go
// Definition of the AddressUpdate model, tracking updates to Addresses

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// AddressUpdate struct represents the AddressUpdatesTable in database.
type AddressUpdate struct {
	gorm.Model            // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	Address    uint       `gorm:"not null;foreignKey:AddressID"` // The address that was updated (foreign key reference to Addresses.Id).
	Type       UpdateType `gorm:"not null"`                      // The type of the update.
	Title      string     `gorm:"not null"`                      // The title of the update.
	UpdatedBy  uint       `gorm:"not null;foreignKey:'UserID'"`  // The user who updated the address (foreign key reference to Users.Id).
	Text       string     `gorm:"type:text"`                     // The text of the update, can be null.
}
