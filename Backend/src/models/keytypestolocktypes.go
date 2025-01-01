// Backend/src/models/keytypestolocktypes.go
// Many to Many relationship between key types and lock types, i.e. which key types can open which lock types

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// KeyTypesToLockTypes defines the structure for the relationship between key types and lock types.
type KeyTypesToLockTypes struct {
	KeyTypeID  uint `gorm:"primaryKey"` // The key type in the relationship.
	LockTypeID uint `gorm:"primaryKey"` // The lock type in the relationship.
}
