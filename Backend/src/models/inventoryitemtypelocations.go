// Backend/src/models/inventoryitemtypelocations.go
// Description: Definition of the InventoryItemTypeLocation model, tracking the locations of inventory items

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// InventoryItemTypeLocations represents the model to track the locations of inventory items.
type InventoryItemTypeLocation struct {
	gorm.Model                            // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	InventoryItemType   InventoryItemType // References InventoryItemType Object
	InventoryItemTypeID uint              `gorm:"not null"` // The key of the inventory item type.
	Location            RoomLocation      // Referenced RoomLocation Object
	LocationID          uint              `gorm:"not null"` // The key of the location.
	Count               int               `gorm:"not null"` // The count of the inventory item type at the location.
}
