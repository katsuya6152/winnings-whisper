package main

import (
	"fmt"
	"dashbord-be/db"
	"dashbord-be/model"
)

func main() {
	dbConn := db.NewDB()
	defer fmt.Println("Successfully Migrated")
	defer db.CloseDB(dbConn)
	dbConn.AutoMigrate(&model.User{})
}