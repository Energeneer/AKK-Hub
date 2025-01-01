// Backend/src/models/itemtaggroupupdates.go
// Definition of the ItemTagGroupUpdate model, tracking updates to item_tag_groups

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// ItemTagGroupUpdates represents updates to item_tag_groups.
type ItemTagGroupUpdate struct {
	gorm.Model              // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	ItemTagGroup int        `gorm:"not null"` // The item_tag_group affected by the update.
	Type         UpdateType `gorm:"not null"` // The type of the update.
	Title        string     `gorm:"not null"` // The title of the update.
	UpdatedBy    int        `gorm:"not null"` // The user reference who updated the item_tag_group.
	Text         *string    // The text of the update.
}
