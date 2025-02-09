package main

import (
	docs "github.com/danmaninc/S25-core-course-labs/app_golang/src/docs"
	"github.com/danmaninc/S25-core-course-labs/app_golang/src/endpoints"
	"github.com/gin-gonic/gin"
	swaggerfiles "github.com/swaggo/files"
	ginSwagger "github.com/swaggo/gin-swagger"
)

// @BasePath /

// The main function.
func main() {
	router := gin.Default()
	docs.SwaggerInfo.BasePath = "/"

	// Load templates
	router.LoadHTMLGlob("src/templates/*")

	// Register endpoints
	v1 := router.Group("/")
	{
		v1.GET("/", endpoints.JokePage)
		v1.GET("/joke", endpoints.Joke)
	}

	// Run router
	router.GET("/swagger/*any", ginSwagger.WrapHandler(swaggerfiles.Handler))
	router.Run(":80")
}
