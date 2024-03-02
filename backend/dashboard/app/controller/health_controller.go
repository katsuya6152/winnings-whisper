package controller

import (
	"net/http"

	"github.com/labstack/echo/v4"
)

type IHealthController interface {
	HealthCheck(c echo.Context) error
}

type healthController struct{}

func NewHealthController() IHealthController {
	return &healthController{}
}

func (hc *healthController) HealthCheck(c echo.Context) error {
	return c.String(http.StatusOK, "OK")
}
