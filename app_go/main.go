package main

import (
	"fmt"
	"net/http"
	"time"

	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()
	r.GET("/", func(c *gin.Context) {
		moscowTime := time.Now().UTC().Add(3 * time.Hour).Format("2006-01-02 15:04:05")
		c.String(http.StatusOK, fmt.Sprintf("Current time in Moscow: %s", moscowTime))
	})
	r.Run(":8080")
}
