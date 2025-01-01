// Backend/src/models/inventoryitemtypeupdates.go
// Definition of the InventoryItemTypeUpdate model, tracking updates to inventory_items

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// InventoryItemTypeUpdates represents the inventory item type updates model.
type InventoryItemTypeUpdate struct {
	gorm.Model                   // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	InventoryItemType int        `gorm:"not null"` // The key affected by the update.
	Type              UpdateType `gorm:"not null"` // The type of the update.
	Title             string     `gorm:"not null"` // The title of the update.
	UpdatedBy         int        `gorm:"not null"` // The user who updated the inventory item type.
	Text              *string    // The text of the update.
}
