package handlers

import (
	"app_go/internal/services"

	"net/http"

	"github.com/gin-gonic/gin"
)

func RenderIndex(c *gin.Context) {
	c.HTML(http.StatusOK, "index.html", nil)
}

func CalculateAge(c *gin.Context) {
	date := c.Query("date")
	age, err := services.CalculateAge(date)
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	c.JSON(http.StatusOK, gin.H{"age": age})
}
