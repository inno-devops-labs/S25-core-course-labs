package main

import (
	"app_go/internal/handlers"

	"github.com/gin-gonic/gin"
)

const PORT = "0.0.0.0:8080"

func main() {
	router := gin.Default()

	router.LoadHTMLGlob("internal/templates/index.html")
	router.Static("/static", "./static")

	// routes
	router.GET("/", handlers.RenderIndex)
	router.GET("/calculate-age", handlers.CalculateAge)

	err := router.Run(PORT)
	if err != nil {
		panic(err)
	}
}
