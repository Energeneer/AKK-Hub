// Backend/src/models/keys.go
// Definition of the Key model

// Author: Valentin Haas, 2025
package models

import (
	"time"

	"gorm.io/gorm"
)

// Key defines the Keys model for the database.
type Key struct {
	gorm.Model                      // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	Type              KeyType       // Referenced KeyRing Object
	TypeID            uint          `gorm:"not null"`        // The type of the key.
	Number            int           `gorm:"not null;unique"` // The number of the key.
	CurrentOwner      *User         // Referenced User Object
	CurrentOwnerID    *uint         // The current owner of the key.
	DefaultLocation   RoomLocation  // Referenced RoomLocation Object
	DefaultLocationID uint          `gorm:"not null"` // The default location of the key.
	CurrentLocation   *RoomLocation // Referenced RoomLocation Object
	CurrentLocationID *uint         // The current location of the key.
	ReceiveByDate     *time.Time    `gorm:"default:null"` // The date the key will be received.
	ReceivedByDate    *time.Time    `gorm:"default:null"` // The date the key was received.
	ReturnByDate      *time.Time    `gorm:"default:null"` // The date the key has to be returned.
	ReturnedByDate    *time.Time    `gorm:"default:null"` // The date the key was returned.
}
