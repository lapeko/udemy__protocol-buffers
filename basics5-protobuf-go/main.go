package main

import (
	p "basics5-protobuf-go/proto"
	"google.golang.org/protobuf/encoding/protojson"
	"google.golang.org/protobuf/proto"
	"google.golang.org/protobuf/types/known/timestamppb"
	"log"
	"os"
	"reflect"
	"time"
)

const fileName = "address_book.txt"

func createPhoneNumber(phoneNumber string, phoneType p.Person_PhoneType) *p.Person_PhoneNumber {
	return &p.Person_PhoneNumber{
		Number: phoneNumber,
		Type:   phoneType,
	}
}

func createPerson(name string, id uint32, email string, phones []*p.Person_PhoneNumber) *p.Person {
	return &p.Person{
		Name:        name,
		Id:          id,
		Email:       email,
		Phones:      phones,
		LastUpdated: &timestamppb.Timestamp{Seconds: time.Now().Unix()},
	}
}

func toJson(message proto.Message) string {
	marshaller := protojson.MarshalOptions{EmitUnpopulated: true}

	json, err := marshaller.Marshal(message)

	if err != nil {
		log.Fatal(err)
	}

	return string(json)
}

func fromJson(json string, t reflect.Type) proto.Message {
	message := reflect.New(t).Interface().(proto.Message)
	if err := protojson.Unmarshal([]byte(json), message); err != nil {
		log.Fatal(err)
	}
	return message
}

func readAddressBookFromFile() *p.AddressBook {
	file, err := os.ReadFile(fileName)
	if err != nil {
		log.Fatal(err)
	}
	addressBook := &p.AddressBook{}
	if err := proto.Unmarshal(file, addressBook); err != nil {
		log.Fatal(err)
	}
	return addressBook
}

func writeAddressBookToFile(book *p.AddressBook) {
	res, err := proto.Marshal(book)
	if err != nil {
		log.Fatal(err)
	}
	if err := os.WriteFile(fileName, res, 0644); err != nil {
		log.Fatal(err)
	}
}

func main() {
	person1 := createPerson(
		"Name 1",
		1,
		"mail1@mai.com",
		[]*p.Person_PhoneNumber{createPhoneNumber("12345", p.Person_HOME)},
	)

	addressBook := &p.AddressBook{People: []*p.Person{person1}}
	json := toJson(addressBook)
	log.Println(json)

	res := fromJson(json, reflect.TypeOf(p.AddressBook{}))

	addressBookRes, ok := res.(*p.AddressBook)

	if !ok {
		log.Fatal("Type casting error")
	}
	log.Println(addressBookRes)

	writeAddressBookToFile(addressBook)
	res = readAddressBookFromFile()
	log.Println(res)
}
