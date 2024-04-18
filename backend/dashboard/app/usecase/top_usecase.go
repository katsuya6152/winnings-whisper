package usecase

import (
	"dashbord-be/model"
	"dashbord-be/repository"
	"fmt"
	"strconv"
	"strings"
	"time"
)

type ITopUsecase interface {
	GetLatestSpiderStats() (model.LatestSpiderStatsRes, error)
}

type topUsecase struct {
	tr  repository.ISpiderStatsRepository
	rr  repository.IRacesRepository
	rrr repository.IRaceResultsRepository
}

func NewTopUsecase(tr repository.ISpiderStatsRepository, rr repository.IRacesRepository, rrr repository.IRaceResultsRepository) ITopUsecase {
	return &topUsecase{tr, rr, rrr}
}

func (tu *topUsecase) GetLatestSpiderStats() (model.LatestSpiderStatsRes, error) {
	stats, err := tu.tr.GetLatestSpiderStats()
	if err != nil {
		return model.LatestSpiderStatsRes{}, err
	}

	race, err := tu.rr.GetLatestRace()
	if err != nil {
		return model.LatestSpiderStatsRes{}, err
	}

	countRaces, err := tu.rr.CountRaces()
	if err != nil {
		return model.LatestSpiderStatsRes{}, err
	}

	countRaceResults, err := tu.rrr.CountRaceResults()
	if err != nil {
		return model.LatestSpiderStatsRes{}, err
	}

	statsRes := model.LatestSpiderStatsRes{
		StartTime:   formatDateTime(stats.StartTime),
		FinishTime:  formatDateTime(stats.FinishTime),
		ElapsedTime: formatElapsedTimeFromString(stats.ElapsedTime),
		StopReason:  findKeywordInString(stats.Reason, "exists in database"),
		Status:      "Success",
		CountRaces:  countRaces,
		CountHorse:  countRaceResults,
		LatestRace:  formatRaceInfo(race.Date),
	}
	return statsRes, nil
}

func formatDateTime(t *time.Time) string {
	if t == nil {
		return ""
	}
	return t.Format("2006/01/02 15:04:05")
}

func formatElapsedTimeFromString(elapsed *string) string {
	if elapsed == nil {
		return ""
	}

	parts := strings.Split(*elapsed, ":")
	if len(parts) < 3 {
		return "時間フォーマットエラー"
	}
	hours, err1 := strconv.Atoi(parts[0])
	minutes, err2 := strconv.Atoi(parts[1])
	seconds, err3 := strconv.Atoi(parts[2])

	if err1 != nil || err2 != nil || err3 != nil {
		return "時間変換エラー"
	}

	result := ""
	if hours > 0 {
		result += fmt.Sprintf("%d時間", hours)
	}
	if minutes > 0 || (hours > 0 && seconds > 0) {
		result += fmt.Sprintf("%d分", minutes)
	}
	result += fmt.Sprintf("%d秒", seconds)

	return result
}

func findKeywordInString(s *string, keyword string) string {
	if s == nil {
		return "Other"
	}
	if strings.Contains(*s, keyword) {
		return keyword
	}
	return "Other"
}

func formatRaceInfo(info *string) string {
	if info == nil || *info == "" {
		return ""
	}

	fmt.Println(*info)

	// " (" もしくは "[" 以降の文字列を削除
	openParenIndex := strings.Index(*info, "(")
	openBracketIndex := strings.Index(*info, "[")

	endIndex := len(*info)
	if openParenIndex != -1 {
		endIndex = openParenIndex
	}
	if openBracketIndex != -1 && openBracketIndex < endIndex {
		endIndex = openBracketIndex
	}

	trimmedInfo := (*info)[:endIndex]

	return insertNewline(trimmedInfo)
}

func insertNewline(info string) string {
	firstSpace := strings.Index(info, " ")
	if firstSpace == -1 {
		return info
	}

	secondSpace := strings.Index(info[firstSpace+1:], " ")
	if secondSpace == -1 {
		return info
	}
	secondSpace += firstSpace + 1

	return info[:secondSpace] + "\n" + info[secondSpace+1:]
}
