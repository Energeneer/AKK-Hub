// Backend/src/models/keys.go
// Definition of the Key model

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
	"time"
)

// Key defines the Keys model for the database.
type Key struct {
	gorm.Model                 // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	Type            uint       `gorm:"not null"`        // The type of the key.
	Number          int        `gorm:"not null;unique"` // The number of the key.
	CurrentOwner    *uint      // The current owner of the key.
	DefaultLocation uint       `gorm:"not null"` // The default location of the key.
	CurrentLocation *uint      // The current location of the key.
	ReceiveByDate   *time.Time `gorm:"default:null"` // The date the key will be received.
	ReceivedByDate  *time.Time `gorm:"default:null"` // The date the key was received.
	ReturnByDate    *time.Time `gorm:"default:null"` // The date the key has to be returned.
	ReturnedByDate  *time.Time `gorm:"default:null"` // The date the key was returned.
}
