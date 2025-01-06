// Backend/src/models/keystolocks.go
// Many to Many relationship between keys and locks, i.e. which keys can open which locks.
// Direct association, should we use an electronic keycard system with individual associations.

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// KeysToLocks defines the relationship model between keys and locks.
type KeysToLocks struct {
	gorm.Model      // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	Key        Key  // Referenced Key Object
	KeyID      uint `gorm:"primaryKey"` // The key in the relationship.
	Lock       Lock // Referenced Lock Object
	LockID     uint `gorm:"primaryKey"` // The lock in the relationship.
}
