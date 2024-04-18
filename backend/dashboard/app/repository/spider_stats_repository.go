package repository

import (
	"dashbord-be/model"
	"fmt"

	"gorm.io/gorm"
)

type ISpiderStatsRepository interface {
	GetLatestSpiderStats() (*model.SpiderStats, error)
}

type spiderStatsRepository struct {
	db *gorm.DB
}

func NewSpiderStatsRepository(db *gorm.DB) ISpiderStatsRepository {
	return &spiderStatsRepository{db}
}

func (tr *spiderStatsRepository) GetLatestSpiderStats() (*model.SpiderStats, error) {
	var latestSpiderStats model.SpiderStats
	err := tr.db.Order("finish_time DESC").First(&latestSpiderStats).Error
	if err != nil {
		fmt.Println("Error fetching latest record:", err)
		return &latestSpiderStats, err
	}
	return &latestSpiderStats, nil
}
