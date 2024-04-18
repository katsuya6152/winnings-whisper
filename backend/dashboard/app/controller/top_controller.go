package controller

import (
	"dashbord-be/usecase"
	"net/http"

	"github.com/labstack/echo/v4"
)

type ITopController interface {
	GetLatestSpiderStats(c echo.Context) error
	GetRaces(c echo.Context) error
}

type topController struct {
	tu usecase.ITopUsecase
}

func NewTopController(tu usecase.ITopUsecase) ITopController {
	return &topController{tu}
}

func (tc *topController) GetLatestSpiderStats(c echo.Context) error {
	spiderStatsRes, err := tc.tu.GetLatestSpiderStats()
	if err != nil {
		return c.JSON(http.StatusInternalServerError, err.Error())
	}
	return c.JSON(http.StatusCreated, spiderStatsRes)
}

func (tc *topController) GetRaces(c echo.Context) error {
	racesRes, err := tc.tu.GetRaces()
	if err != nil {
		return c.JSON(http.StatusInternalServerError, err.Error())
	}
	return c.JSON(http.StatusCreated, racesRes)
}
