// Backend/src/models/locktypes.go
// Definition of the LockType model

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// LockTypes defines the structure for representing lock types.
type LockType struct {
	gorm.Model         // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	Name        string `gorm:"not null"`     // The name of the lock type.
	Description string `gorm:"default:null"` // The description of the lock type.
}
