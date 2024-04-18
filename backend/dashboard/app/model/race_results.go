package model

type RaceResult struct {
	HorseID      string  `gorm:"type:varchar(45);not null;primaryKey" json:"horse_id"` // 主キー
	ID           string  `gorm:"type:varchar(45);not null" json:"race_id"`             // races(id) に外部キーとして関連づける場合は設定が必要
	Rank         *string `gorm:"type:varchar(45);" json:"rank,omitempty"`              // 競走結果の順位
	Box          *string `gorm:"type:varchar(45);" json:"box,omitempty"`               // 競走馬のボックス番号
	HorseOrder   *string `gorm:"type:varchar(45);" json:"order,omitempty"`             // 競走馬のオーダー
	HorseName    *string `gorm:"type:varchar(45);" json:"name,omitempty"`              // 競走馬の名前
	SexAndAge    *string `gorm:"type:varchar(45);" json:"sex_and_age,omitempty"`       // 性別と年齢
	BurdenWeight *string `gorm:"type:varchar(45);" json:"burden_weight,omitempty"`     // 負担重量
	Jockey       *string `gorm:"type:varchar(45);" json:"jockey,omitempty"`            // 騎手
	Time         *string `gorm:"type:varchar(45);" json:"time,omitempty"`              // タイム
	Difference   *string `gorm:"type:varchar(45);" json:"difference,omitempty"`        // タイム差
	Transit      *string `gorm:"type:varchar(45);" json:"transit,omitempty"`           // 通過
	Climb        *string `gorm:"type:varchar(45);" json:"climb,omitempty"`             // 上り（クライム）
	Odds         *string `gorm:"type:varchar(45);" json:"odds,omitempty"`              // オッズ
	Popularity   *string `gorm:"type:varchar(45);" json:"popularity,omitempty"`        // 人気
	HorseWeight  *string `gorm:"type:varchar(45);" json:"horse_weight,omitempty"`      // 馬体重
	HorseTrainer *string `gorm:"type:varchar(45);" json:"trainer,omitempty"`           // 調教師
	HorseOwner   *string `gorm:"type:varchar(90);" json:"owner,omitempty"`             // 馬の所有者
	Prize        *string `gorm:"type:varchar(45);" json:"prize,omitempty"`
}
