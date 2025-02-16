package routes

import (
	"app_go/internal/http_client"
	"net/http"
	"time"

	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"
)

func RegisterRoutes() http.Handler {
	e := echo.New()

	e.Use(middleware.Logger())
	e.Use(middleware.Recover())

	client := http_client.New(&http.Client{Timeout: 2 * time.Second})

	e.GET("/price", GetPriceHandler(client))

	return e
}
