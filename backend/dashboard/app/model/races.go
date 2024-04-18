package model

type Race struct {
	ID              string  `gorm:"type:varchar(45);primaryKey" json:"id"`
	RaceName        string  `gorm:"type:varchar(45);not null" json:"race_name"`
	RacePlace       *string `gorm:"type:varchar(45)" json:"race_place,omitempty"`
	NumberOfEntries *int    `gorm:"default:null" json:"number_of_entries,omitempty"`
	RaceState       *string `gorm:"type:varchar(45)" json:"race_state,omitempty"`
	Date            *string `gorm:"type:varchar(45)" json:"date,omitempty"`
}

type RaceRes struct {
	RaceName        string `json:"race_name"`
	RacePlace       string `json:"race_place"`
	NumberOfEntries int    `json:"number_of_entries"`
	Date            string `json:"date"`
}
