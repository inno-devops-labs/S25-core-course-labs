package endpoints

import (
	"net/http"

	"github.com/danmaninc/S25-core-course-labs/app_golang/src/utils"
	"github.com/gin-gonic/gin"
)

// @BasePath /

// Visits godoc
// @Summary Returns number of times the app accessed
// @Schemes
// @Description Returns number of times the app accessed
// @Tags visits
// @Accept json
// @Produce json
// @Success 200 {string} html
// @Router /visits [get]
func Visits(c *gin.Context) {
	c.JSON(http.StatusOK, utils.Counter)
}
