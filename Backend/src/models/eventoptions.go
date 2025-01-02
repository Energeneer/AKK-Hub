// Backend/src/models/eventoptions.go
// Definition of the EventOptions model, tracking the options for events.

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// EventOptionsModel to track the options for events.
type EventOption struct {
	gorm.Model          // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	Event       uint    `gorm:"not null; foreignKey:EventID"` // The event the option belongs to.
	Title       string  `gorm:"not null"`                     // The title of the option.
	CostCt      int     `gorm:"not null"`                     // The cost of the option in cents.
	Description *string `gorm:"type:text;default:null"`       // The description of the option.
	IsOptional  bool    `gorm:"not null;default:true"`        // Whether the option is optional or not.
}
