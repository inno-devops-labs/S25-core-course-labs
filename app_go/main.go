package main

import (
	"html/template"
	"math/rand"
	"net/http"
	"strconv"
	"time"

	"github.com/gin-gonic/gin"
)

var secretNumber int

var rng = rand.New(rand.NewSource(time.Now().UnixNano()))

func main() {
	r := setupRouter()
	if err := r.Run(":8080"); err != nil {
		panic(err)
	}
}

func setupRouter() *gin.Engine {
	gin.SetMode(gin.ReleaseMode)
	r := gin.Default()

	resetSecretNumber()

	r.SetHTMLTemplate(template.Must(template.New("index").Parse(`
		<!DOCTYPE html>
		<html lang="en">
		<head><title>Guess the Number</title></head>
		<body>{{.Feedback}}</body>
		</html>
	`)))

	r.GET("/", func(c *gin.Context) {
		c.HTML(http.StatusOK, "index", gin.H{"Feedback": nil})
	})

	r.POST("/", func(c *gin.Context) {
		guessStr := c.PostForm("guess")
		guess, err := strconv.Atoi(guessStr)
		if err != nil {
			c.HTML(http.StatusBadRequest, "index", gin.H{"Feedback": "Invalid input. Please enter a number."})
			return
		}

		var feedback string
		if guess < secretNumber {
			feedback = "Too Low!"
		} else if guess > secretNumber {
			feedback = "Too High!"
		} else {
			feedback = "Correct! You guessed the number!"
			resetSecretNumber()
		}

		c.HTML(http.StatusOK, "index", gin.H{"Feedback": feedback})
	})

	return r
}

func resetSecretNumber() {
	secretNumber = rng.Intn(100) + 1
}
