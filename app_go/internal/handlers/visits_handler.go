package handlers

import (
	"net/http"

	"app_go/internal/services"

	"github.com/gin-gonic/gin"
)

func GetVisits(c *gin.Context) {
	count, err := services.ReadVisits()
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	c.JSON(http.StatusOK, gin.H{"visits": count})
}
