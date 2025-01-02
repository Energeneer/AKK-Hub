// Backend/src/models/updates.go
// Definitions for update tracking in the database

// Author: Valentin Haas, 2025
package models

// UpdateType is an enumeration of the different types of updates.
type UpdateType int

const (
	OTHERUPDATETYPE UpdateType = iota // An update of unknown type.
	VAL_ADDITION                      // An addition of a new value.
	VAL_REMOVAL                       // A removal of a value.
	VAL_CHANGE                        // A change of a value.
	REF_ADDITION                      // An addition of a reference.
	REF_REMOVAL                       // A removal of a reference.
	REF_CHANGE                        // A change of a reference.
)
