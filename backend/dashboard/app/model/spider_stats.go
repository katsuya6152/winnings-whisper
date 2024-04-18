package model

import "time"

type SpiderStats struct {
	ID          uint       `json:"id" gorm:"primaryKey"`
	SpiderName  *string    `json:"spider_name"`
	StartTime   *time.Time `json:"start_time"`
	FinishTime  *time.Time `json:"finish_time"`
	ElapsedTime *string    `gorm:"type:time" json:"elapsed_time"`
	Reason      *string    `json:"reason"`
	Stats       *string    `json:"stats"`
}

type LatestSpiderStatsRes struct {
	StartTime   string `json:"start_time"`
	FinishTime  string `json:"finish_time"`
	ElapsedTime string `json:"elapsed_time"`
	StopReason  string `json:"stop_reason"`
	Status      string `json:"status"`
	CountRaces  int64  `json:"count_races"`
	CountHorse  int64  `json:"count_horse"`
	LatestRace  string `json:"latest_race"`
}
