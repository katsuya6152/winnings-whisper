package main

import (
	"dashbord-be/controller"
	"dashbord-be/db"
	"dashbord-be/repository"
	"dashbord-be/router"
	"dashbord-be/usecase"
	"dashbord-be/validator"
)

func main() {
	db := db.NewDB()
	userValidator := validator.NewUserValidator()
	userRepository := repository.NewUserRepository(db)
	userUsecase := usecase.NewUserUsecase(userRepository, userValidator)
	userController := controller.NewUserController(userUsecase)
	healthController := controller.NewHealthController()
	e := router.NewRouter(healthController, userController)
	e.Logger.Fatal(e.Start(":8080"))
}
