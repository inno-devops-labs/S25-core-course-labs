package main

import (
	"path/filepath"

	docs "github.com/danmaninc/S25-core-course-labs/app_golang/src/docs"
	"github.com/danmaninc/S25-core-course-labs/app_golang/src/endpoints"
	"github.com/danmaninc/S25-core-course-labs/app_golang/src/utils"
	"github.com/gin-gonic/gin"
	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promhttp"
	swaggerfiles "github.com/swaggo/files"
	ginSwagger "github.com/swaggo/gin-swagger"
)

var jokePageCounter = prometheus.NewGauge(prometheus.GaugeOpts{
	Name: "joke_page_visits",
	Help: "Count of received jokes via webpage. Bring humour to the world!",
})

var jokeJsonCounter = prometheus.NewGauge(prometheus.GaugeOpts{
	Name: "joke_json_visits",
	Help: "Count of received jokes via API endpoint. Bring humour to the robots!",
})

func init() {
	prometheus.MustRegister(jokePageCounter, jokeJsonCounter)
}

func prometheusHandler() gin.HandlerFunc {
	h := promhttp.Handler()

	return func(c *gin.Context) {
		h.ServeHTTP(c.Writer, c.Request)
	}
 }
// @BasePath /

func setupRouter() *gin.Engine {
	jokePageCounter.Set(0)
	jokeJsonCounter.Set(0)

	router := gin.Default()
	docs.SwaggerInfo.BasePath = "/"

	// Load templates
	router.LoadHTMLGlob(filepath.Join("./src", "templates/*"))

	// Register endpoints
	v1 := router.Group("/")
	{
		v1.GET("/", endpoints.JokePage, func (c *gin.Context) { jokePageCounter.Inc(); utils.IncrementCounter() })
		v1.GET("/joke", endpoints.Joke, func (c *gin.Context) { jokeJsonCounter.Inc(); utils.IncrementCounter() })
		v1.GET("/visits", endpoints.Visits)
	}

	// Run router
	router.GET("/swagger/*any", ginSwagger.WrapHandler(swaggerfiles.Handler))

	router.GET("/metrics", prometheusHandler())

	return router
}

// The main function.
func main() {
	router := setupRouter()
	
	router.Run(":80")
}
