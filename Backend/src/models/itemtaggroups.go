// Backend/src/models/itemtaggroups.go
// Description: Item tag groups model.

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// ItemTagGroups represents the item tag groups.
type ItemTagGroup struct {
	gorm.Model          // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	Name        string  `gorm:"size:64;not null"` // The name of the item tag group.
	Description *string // The description of the item tag group.
}
