package endpoints

import (
	"net/http"

	"github.com/danmaninc/S25-core-course-labs/app_golang/src/utils"
	"github.com/gin-gonic/gin"
)

// @BasePath /

// JokePage godoc
// @Summary Returns a web page with the random joke
// @Schemes
// @Description Returns a web page with the random joke
// @Tags joke
// @Accept json
// @Produce json
// @Success 200 {string} html
// @Router / [get]
func JokePage(c *gin.Context) {
	joke := utils.JokeFromAPI(c)

	if joke.Type == "twopart" {
		c.HTML(http.StatusOK, "joke.tmpl", gin.H{
			"joke": joke.Setup + " " + joke.Delivery,
		})
	} else {
		c.HTML(http.StatusOK, "joke.tmpl", gin.H{
			"joke": joke.Joke,
		})
	}
}
