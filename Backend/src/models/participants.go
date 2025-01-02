// Backend/src/models/participants.go
// Definition of the Participant model, tracking participants in events.

// Author: Valentin Haas, 2025
package models

import (
	"gorm.io/gorm"
)

// ParticipantRoles enum to define the roles of participants in events.
type ParticipantRoles int

const (
	OTHERROLE   ParticipantRoles = iota // The participant has another role in the event.
	ORGANIZER                           // The participant is an organizer of the event.
	SPEAKER                             // The participant is a speaker at the event.
	PARTICIPANT                         // The participant is a participant in the event.
	VISITOR                             // The participant is a visitor of the event.
	BAND                                // The participant is a band at the event.
	SPONSOR                             // The participant is a sponsor of the event.
)

// Participants is a model to track participants in events.
type Participant struct {
	gorm.Model                                    // Provides ID, CreatedAt, UpdatedAt, DeletedAt fields
	User                         int              `gorm:"primaryKey"`        // The unique identifier of the user.
	Event                        int              `gorm:"primaryKey"`        // The unique identifier of the event.
	Role                         ParticipantRoles `gorm:"type:int;not null"` // The role of the participant in the event.
	Organisation                 *int             // The organisation of the participant in the event.
	ChosenItems                  *int             // The chosen items of the participant in the event.
	PayedAmountCt                int              `gorm:"not null;default:0"`     // The amount payed by the participant in cents.
	HasAcceptedEventRequirements bool             `gorm:"not null;default:false"` // Indicates whether the participant has accepted the event requirements.
}
