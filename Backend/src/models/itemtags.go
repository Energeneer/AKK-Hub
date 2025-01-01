// Backend/src/models/itemtags.go
// Definition of the ItemTag model, tracking the tags of inventory items

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// ItemTags represents tags of inventory items.
type ItemTag struct {
	gorm.Model          // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	Name        string  `gorm:"not null"` // The name of the tag.
	TagGroup    *int    // The tag group the tag is associated with.
	Description *string // The description of the tag.
}
