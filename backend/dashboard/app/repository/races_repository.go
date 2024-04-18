package repository

import (
	"dashbord-be/model"
	"fmt"

	"gorm.io/gorm"
)

type IRacesRepository interface {
	GetLatestRace() (*model.Race, error)
	GetLatestRaces(limit int) ([]model.Race, error)
	CountRaces() (int64, error)
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

func (tr *racesRepository) GetLatestRaces(limit int) ([]model.Race, error) {
	var races []model.Race
	err := tr.db.Order("date DESC").Limit(limit).Find(&races).Error
	if err != nil {
		fmt.Println("Error fetching latest races:", err)
		return nil, err
	}
	return races, nil
}

func (tr *racesRepository) CountRaces() (int64, error) {
	var count int64
	err := tr.db.Model(&model.Race{}).Count(&count).Error
	if err != nil {
		fmt.Println("Error counting race records:", err)
		return 0, err
	}
	return count, nil
}
