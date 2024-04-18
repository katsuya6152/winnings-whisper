package repository

import (
	"dashbord-be/model"
	"fmt"

	"gorm.io/gorm"
)

type IRaceResultsRepository interface {
	CountRaceResults() (int64, error)
}

type raceResultsRepository struct {
	db *gorm.DB
}

func NewRaceResultsRepository(db *gorm.DB) IRaceResultsRepository {
	return &raceResultsRepository{db}
}

func (tr *raceResultsRepository) CountRaceResults() (int64, error) {
	var count int64
	err := tr.db.Model(&model.RaceResult{}).Count(&count).Error
	if err != nil {
		fmt.Println("Error counting race result records:", err)
		return 0, err
	}
	return count, nil
}
