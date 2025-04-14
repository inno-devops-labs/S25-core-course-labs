package main

import (
    "math/rand"
	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()
    phrases := []string{
        "It is time to be produnctive.",
        "I think you need to relax for a time.",
        "Sport is what you need",
        "Maybe art would help you to deal with stress?",
        "There are so many people around. Maybe you need to make new friends?",
        "You are very close to your dream!",
        "Be yourself and everything will be fine!",
        "Do not lose your beautiful smile!",
        "You are on your right path.",
        "All will be fine, just wait a little bit",
    }
    
    r.GET("/", func(c *gin.Context) {
        randomIndex := rand.Intn(len(phrases))
        c.JSON(200, gin.H{
            "quote": phrases[randomIndex],
        })
    })

	r.Run(":8080")
}
