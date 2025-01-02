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
	ItemTagGroup uint       `gorm:"not null;foreignKey:ItemTagGroupID"` // The item tag group that was updated (foreign key reference to ItemTagGroups.Id).
	Type         UpdateType `gorm:"not null"`                           // The type of the update.
	Title        string     `gorm:"not null"`                           // The title of the update.
	UpdatedBy    uint       `gorm:"not null;foreignKey:UserID"`         // The user who updated the group (foreign key reference to Users.Id).
	Text         *string    // The text of the update.
}
