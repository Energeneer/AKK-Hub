// Backend/src/models/roominflucences.go
// Description: Room influences model for storing how room occupation affects other rooms.

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// RoomInfluences is a model for the database.
type RoomInfluence struct {
	gorm.Model             // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	OccupiedRoom      int  `gorm:"not null"`               // The room that is occupied.
	AffectedRoom      int  `gorm:"not null"`               // The room that is affected by the occupation.
	AffectsAccess     bool `gorm:"not null;default:false"` // Whether the occupation affects access to the room.
	AffectsSound      bool `gorm:"not null;default:false"` // Whether the occupation affects sound in the room.
	AffectsSmell      bool `gorm:"not null;default:false"` // Whether the occupation affects smell in the room.
	AffectsOccupation bool `gorm:"not null;default:false"` // Whether the occupation affects occupation of the room.
}
