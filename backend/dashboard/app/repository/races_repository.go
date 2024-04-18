package repository

import (
	"dashbord-be/model"
	"fmt"

	"gorm.io/gorm"
)

type IRacesRepository interface {
	GetLatestRace() (*model.Race, error)
}

type racesRepository struct {
	db *gorm.DB
}

func NewRacesRepository(db *gorm.DB) IRacesRepository {
	return &racesRepository{db}
}

func (tr *racesRepository) GetLatestRace() (*model.Race, error) {
	var latestRace model.Race
	err := tr.db.Order("date DESC").First(&latestRace).Error
	if err != nil {
		fmt.Println("Error fetching latest record:", err)
		return &latestRace, err
	}
	return &latestRace, nil
}
