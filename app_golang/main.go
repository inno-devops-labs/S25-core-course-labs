package main

import (
	"github.com/gin-gonic/gin"
	"net/http"
	"time"
)

func main() {
	location, err := time.LoadLocation("Europe/Moscow")
	if err != nil {
		panic(err)
	}

	r := gin.Default()
	r.GET("/time", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"time": time.Now().In(location),
		})
	})
	r.Run()
}
