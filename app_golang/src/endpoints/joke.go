package endpoints

import (
	"net/http"

	"github.com/danmaninc/S25-core-course-labs/app_golang/src/utils"
	"github.com/gin-gonic/gin"
)

type JokeResponse struct {
	Joke string
}

// @BasePath /

// Joke godoc
// @Summary Returns a random joke in JSON format
// @Schemes
// @Description Returns a random joke in JSON format
// @Tags joke
// @Accept json
// @Produce json
// @Success 200 {object} JokeResponse
// @Router /joke [get]
func Joke(c *gin.Context) {
	joke := utils.JokeFromAPI(c)

	if joke.Type == "twopart" {
		c.JSON(http.StatusOK, gin.H{
			"joke": joke.Setup + " " + joke.Delivery,
		})
	} else {
		c.JSON(http.StatusOK, gin.H{
			"joke": joke.Joke,
		})
	}
}
