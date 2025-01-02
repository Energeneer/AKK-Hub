// Backend/src/models/itemtagstoinventoryitemtypes.go
// Many-to-many relationship between item tags and inventory item types.

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// ItemTagsToInventoryItemTypes represents a many-to-many relationship between item tags and inventory item types.
type ItemTagsToInventoryItemType struct {
	gorm.Model             // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	ItemTag           uint `gorm:"primaryKey; not null; foreignKey:ItemTagID"`           // The item tag of the relationship.
	InventoryItemType uint `gorm:"primaryKey; not null; foreignKey:InventoryItemTypeID"` // The inventory item type of the relationship.
}
