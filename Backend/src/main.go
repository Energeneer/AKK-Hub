package main

import (
	"log"

	"gorm.io/driver/sqlite"
	"gorm.io/gorm"

	"akk/hub/models"
)

func main() {
	db, err := gorm.Open(sqlite.Open("test.db"), &gorm.Config{})
	if err != nil {
		log.Fatal(err)
	}

	db.AutoMigrate(
		&models.AddressEmail{},
		&models.Address{},
		&models.AddressTelNumber{},
		&models.AddressUpdate{},
		&models.Building{},
		&models.BuildingUpdate{},
		&models.DBVersion{},
		&models.Email{},
		&models.EventOption{},
		&models.EventOptionUpdate{},
		&models.Event{},
		&models.EventUpdate{},
		&models.Group{},
		&models.GroupUpdate{},
		&models.InventoryItemTypeLocation{},
		&models.InventoryItemType{},
		&models.InventoryItemTypeUpdate{},
		&models.ItemReservation{},
		&models.ItemReservationUpdate{},
		&models.ItemTagGroup{},
		&models.ItemTagGroupUpdate{},
		&models.ItemTag{},
		&models.ItemTagsToInventoryItemType{},
		&models.ItemTypeCategory{},
		&models.KeyRing{},
		&models.KeyRingUpdate{},
		&models.Key{},
		&models.KeysToLocks{},
		&models.KeyType{},
		&models.KeyTypesToLockTypes{},
		&models.KeyTypeUpdate{},
		&models.KeyUpdate{},
		&models.LinkedSite{},
		&models.Lock{},
		&models.LockType{},
		&models.LockTypeUpdate{},
		&models.LockUpdate{},
		&models.OrganisationAddresse{},
		&models.OrganisationEmail{},
		&models.OrganisationLinkedSite{},
		&models.Organisation{},
		&models.OrganisationTelNumber{},
		&models.OrganisationUpdate{},
		&models.Participant{},
		&models.ParticipantUpdate{},
		&models.Role{},
		&models.RoleUpdate{},
		&models.RoomInfluence{},
		&models.RoomInflucenceUpdate{},
		&models.RoomLocation{},
		&models.RoomLocationUpdate{},
		&models.RoomReservation{},
		&models.RoomReservationUpdate{},
		&models.Room{},
		&models.RoomUpdate{},
		&models.TelephoneNumber{},
		&models.TimeFrame{},
		&models.TimeFrameUpdate{},
		&models.TimeSeries{},
		&models.TimeSeriesUpdate{},
		&models.UserAddress{},
		&models.UserEmail{},
		&models.UserGroup{},
		&models.UserLinkedSite{},
		&models.UserOrganisation{},
		&models.UserRole{},
		&models.User{},
		&models.UserTelNumber{},
		&models.UserUpdate{},
	)
}
