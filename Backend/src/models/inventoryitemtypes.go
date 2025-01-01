// Backend/src/models/inventoryitemtypes.go
// Description: Inventory item types model.

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// InventoryItemTypes represents the inventory item types model.
type InventoryItemType struct {
	gorm.Model                // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	Name              string  `gorm:"size:64;not null"` // The name of the inventory item type.
	Category          *int    // The category of the inventory item type.
	DefaultLocation   int     `gorm:"not null"`               // The default location of the inventory item type.
	IsRentable        bool    `gorm:"not null;default:false"` // Whether the inventory item type is rentable.
	Description       *string // The description of the inventory item type.
	ImagePath         *string // The image path of the inventory item type.
	AmountExisting    *int    // The amount of existing inventory items of this type.
	AmountAvailable   *int    // The amount of available inventory items of this type.
	PriceCt           *int    // The price of the inventory item type in cents.
	ReplacementCostCt *int    // The replacement cost of the inventory item type in cents.
	Specifications    *string // The specifications of the inventory item type.
	Comment           *string // A comment on the inventory item type.
}
