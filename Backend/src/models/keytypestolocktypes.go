// Backend/src/models/keytypestolocktypes.go
// Many to Many relationship between key types and lock types, i.e. which key types can open which lock types

// Author: Valentin Haas, 2025
package models

import "time"

// KeyTypesToLockTypes defines the structure for the relationship between key types and lock types.
type KeyTypesToLockTypes struct {
	KeyType    KeyType   // Referenced KeyType Object
	KeyTypeID  uint      `gorm:"primaryKey"` // The key type in the relationship.
	LockType   LockType  // Referenced LockType Object
	LockTypeID uint      `gorm:"primaryKey"` // The lock type in the relationship.
	CreatedAt  time.Time // Time the model was created. Auto Populated by Gorm.
	UpdatedAt  time.Time // Time the model was updated. Auto Populated by Gorm.
	DeletedAt  time.Time // Time the model was deleted. Auto Populated by Gorm.
}
