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
	spiderStatsRepository := repository.NewSpiderStatsRepository(db)
	racesRepository := repository.NewRacesRepository(db)
	raceResultsRepository := repository.NewRaceResultsRepository(db)
	topUsecase := usecase.NewTopUsecase(spiderStatsRepository, racesRepository, raceResultsRepository)
	topController := controller.NewTopController(topUsecase)
	e := router.NewRouter(healthController, userController, topController)
	e.Logger.Fatal(e.Start(":8080"))
}
