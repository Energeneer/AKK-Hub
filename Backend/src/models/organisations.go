// Backend/src/models/users.go
// Definition of the User model

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// Organisations is a model representing an organisation in the database.
type Organisation struct {
	gorm.Model            // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	Name           string `gorm:"unique;not null"` // The name of the organisation.
	Description    string `gorm:"type:text"`       // The description of the organisation.
	IsStudentic    bool   `gorm:"default:false"`   // Whether the organisation is a Studentic organisation.
	IsBlocked      bool   `gorm:"default:true"`    // Whether the organisation is blocked.
	InternalRemark string `gorm:"type:text"`       // An internal remark about the organisation.
}
