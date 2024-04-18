package router

import (
	"dashbord-be/controller"
	// "net/http"
	"os"

	echojwt "github.com/labstack/echo-jwt/v4"
	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"
)

func NewRouter(hc controller.IHealthController, uc controller.IUserController, tc controller.ITopController) *echo.Echo {
	e := echo.New()
	e.Use(middleware.CORSWithConfig(middleware.CORSConfig{
		AllowOrigins: []string{"http://localhost:3000", os.Getenv("FE_URL")},
		AllowHeaders: []string{echo.HeaderOrigin, echo.HeaderContentType, echo.HeaderAccept,
			echo.HeaderAccessControlAllowHeaders, echo.HeaderXCSRFToken},
		AllowMethods:     []string{"GET", "PUT", "POST", "DELETE"},
		AllowCredentials: true,
	}))
	// e.Use(middleware.CSRFWithConfig(middleware.CSRFConfig{
	// 	CookiePath:     "/",
	// 	CookieDomain:   os.Getenv("API_DOMAIN"),
	// 	CookieHTTPOnly: true,
	// 	// CookieSameSite: http.SameSiteNoneMode,
	// 	CookieSameSite: http.SameSiteDefaultMode,
	// 	//CookieMaxAge:   60,
	// }))
	e.GET("/health", hc.HealthCheck)
	e.POST("/signup", uc.SignUp)
	e.POST("/login", uc.LogIn)
	e.POST("/logout", uc.LogOut)
	e.GET("/csrf", uc.CsrfToken)
	t := e.Group("/tasks")
	t.Use(echojwt.WithConfig(echojwt.Config{
		SigningKey:  []byte(os.Getenv("SECRET")),
		TokenLookup: "cookie:token",
	}))
	e.GET("/top/spider-stats/latest", tc.GetLatestSpiderStats)
	return e
}
