// Backend/src/models/roominflucences.go
// Description: Room influences model for storing how room occupation affects other rooms.

// Author: Valentin Haas, 2025
package models

import "time"

// RoomInfluences is a model for the database.
type RoomInfluence struct {
	OccupiedRoom      Room      // Referenced Room Object
	OccupiedRoomID    uint      `gorm:"primaryKey"` // The room that is occupied.
	AffectedRoom      Room      // Referenced Room Object
	AffectedRoomID    uint      `gorm:"primaryKey"` // The room that is affected by the occupation.
	CreatedAt         time.Time // Time the model was created. Auto Populated by Gorm.
	UpdatedAt         time.Time // Time the model was updated. Auto Populated by Gorm.
	DeletedAt         time.Time // Time the model was deleted. Auto Populated by Gorm.
	AffectsAccess     bool      `gorm:"not null;default:false"` // Whether the occupation affects access to the room.
	AffectsSound      bool      `gorm:"not null;default:false"` // Whether the occupation affects sound in the room.
	AffectsSmell      bool      `gorm:"not null;default:false"` // Whether the occupation affects smell in the room.
	AffectsOccupation bool      `gorm:"not null;default:false"` // Whether the occupation affects occupation of the room.
}
