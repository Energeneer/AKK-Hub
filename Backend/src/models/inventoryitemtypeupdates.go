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
	InventoryItemType uint       `gorm:"not null;foreignKey:InventoryItemTypeID"` // The inventory item type that was updated (foreign key reference to InventoryItemTypes.Id).
	Type              UpdateType `gorm:"not null"`                                // The type of the update.
	Title             string     `gorm:"not null"`                                // The title of the update.
	UpdatedBy         uint       `gorm:"not null;foreignKey:UserID"`              // The user who updated the group (foreign key reference to Users.Id).
	Text              *string    // The text of the update.
}
