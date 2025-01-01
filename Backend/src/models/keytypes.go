// Backend/src/models/keytypes.go
// Definition of the Key Type model: What types of keys are available for the system

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// KeyTypes defines the structure for the database model of key types.
type KeyType struct {
	gorm.Model           // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	Name         string  `gorm:"not null"`     // The name of the key type.
	Description  *string `gorm:"type:text"`    // The description of the key type.
	HangerNumber *int    `gorm:"default:null"` // The number of the key hanger within the key cabinet.
}
