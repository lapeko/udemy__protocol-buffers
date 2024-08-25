package main

import (
	pb "basics5-protobuf-go/proto"
	"fmt"
)

func getSimple() *pb.SimpleMessage {
	return &pb.SimpleMessage{
		Id:       42,
		IsSimple: true,
		Name:     "Some name",
		Numbers:  []int32{1, 2, 3, 4},
	}
}

func main() {
	simple := getSimple()
	fmt.Printf("Id: %d\nName: %s\nIsSimple: %t\nNumbers: %v", simple.Id, simple.Name, simple.IsSimple, simple.Numbers)
}
