// Backend/src/models/roominflucenceupdates.go
// Definition of the RoomInflucenceUpdate model, tracking updates to room_influcences

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// RoomInflucenceUpdates is a model to track the updates of RoomInfluences.
type RoomInflucenceUpdate struct {
	gorm.Model                                // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	RoomInfluence               RoomInfluence // Referenced RoomInfluence Object
	RoomInfluenceOccupiedRoomID uint          `gorm:"not null"` // The RoomInfluence that was updated (foreign key reference to RoomInfluences.OccupiedRoomID).
	RoomInfluenceAffectedRoomID uint          `gorm:"not null"` // The RoomInfluence that was updated (foreign key reference to RoomInfluences.AffectedRoomID).
	Type                        UpdateType    `gorm:"not null"` // The type of the update.
	Title                       string        `gorm:"not null"` // The title of the update.
	UpdatedBy                   User          // Referenced User Object
	UpdatedByID                 uint          `gorm:"not null"`     // The user who updated the group (foreign key reference to Users.Id).
	Text                        string        `gorm:"default:null"` // The text of the update.
}
