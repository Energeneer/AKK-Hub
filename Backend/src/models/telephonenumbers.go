// Backend/src/models/telephonenumbers.go
// Definition of the TelephoneNumber model

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// TelephoneNumberType defines the type enumeration for telephone numbers.
type TelephoneNumberType int

const (
	OTHER_TEL_NUMBER_TYPE TelephoneNumberType = iota // The telephone number is of another type.
	HOME                                             // The telephone number is a home number.
	MOBILE                                           // The telephone number is a mobile number.
	WORK                                             // The telephone number is a work number.
	FAX                                              // The telephone number is a fax number.
)

// TelephoneNumbers defines the TelephoneNumber model for the database.
type TelephoneNumber struct {
	gorm.Model                     // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	Number     string              `gorm:"not null"` // The number of the telephone number.
	Label      string              `gorm:"not null"` // The label of the telephone number.
	Type       TelephoneNumberType `gorm:"not null"` // The type of the telephone number.
}
