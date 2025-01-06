// Backend/src/models/locks.go
// Definition of the Lock model

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// Locks defines the structure for representing locks.
type Lock struct {
	gorm.Model                     // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	Type              LockType     // Referenced LockType Object
	TypeID            uint         `gorm:"not null"`        // The type of the lock.
	Number            int          `gorm:"not null;unique"` // The number of the lock.
	DefaultLocation   RoomLocation // Referenced RoomLocation Object
	DefaultLocationID uint         `gorm:"not null"` // The default location of the lock.
	CurrentLocation   RoomLocation // Referenced RoomLocation
	CurrentLocationID uint         `gorm:"not null"` // The current location of the lock.
}
