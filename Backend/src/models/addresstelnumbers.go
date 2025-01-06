// Backend/src/models/addresstelnumbers.go
// Definition of the AddressTelNumbers model that connects addresses and telephone numbers.

// Author: Valentin Haas, 2025
package models

import (
	"time"
)

// AddressTelNumbers represents the connection between addresses and telephone numbers.
type AddressTelNumber struct {
	Address     Address
	AddressID   uint            `gorm:"primaryKey"` // The unique identifier of the address, acts as part of composite primary key.
	TelNumber   TelephoneNumber // Referenced TelephoneNumer Object
	TelNumberID uint            `gorm:"primaryKey"` // The unique identifier of the telephone number, acts as part of composite primary key.
	CreatedAt   time.Time       // Time the model was created. Auto Populated by Gorm.
	UpdatedAt   time.Time       // Time the model was updated. Auto Populated by Gorm.
	DeletedAt   time.Time       // Time the model was deleted. Auto Populated by Gorm.
	IsPrimary   bool            `gorm:"not null"` // Indicates whether it's the primary telephone number for the address.
}
