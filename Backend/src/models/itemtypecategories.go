// Backend/src/models/itemtypecategories.go
// Definition of the ItemTypeCategory model, tracking the categories of inventory item types

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// ItemTypeCategory represents the categories of inventory item types.
type ItemTypeCategory struct {
	gorm.Model          // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	Name        string  `gorm:"not null"`  // The name of the item type category.
	Description *string `gorm:"type:text"` // The description of the item type category, optional.
}
