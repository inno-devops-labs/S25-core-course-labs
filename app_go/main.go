package main

import (
	"fmt"
	"html/template"
	"io"
	"log"
	"math/rand"
	"net/http"
	"os"
	"strconv"
	"time"

	"github.com/gin-gonic/gin"
)

var secretNumber int

var rng = rand.New(rand.NewSource(time.Now().UnixNano()))

var logger *log.Logger

func main() {
	logFile, err := os.OpenFile("/var/log/app_logs/go_app.log", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0666)
	if err != nil {
		fmt.Println("Failed to open log file:", err)
		return
	}

	multiWriter := io.MultiWriter(logFile, os.Stdout)

	logger = log.New(multiWriter, "", log.LstdFlags)

	r := setupRouter()
	logger.Println("Gin App started on port 8080")

	if err := r.Run(":8080"); err != nil {
		logger.Fatalf("Error starting server: %v", err)
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
		<body>
			<h1>Guess the Number (1-100)</h1>
			{{if .Feedback}}
				<p><strong>{{.Feedback}}</strong></p>
			{{end}}
			<form method="POST">
				<label for="guess">Enter your guess:</label>
				<input type="number" id="guess" name="guess" required>
				<button type="submit">Submit</button>
			</form>
		</body>
		</html>
	`)))

	r.GET("/", func(c *gin.Context) {
		logger.Println("GET request on home page received")
		c.HTML(http.StatusOK, "index", gin.H{"Feedback": nil})
	})

	r.POST("/", func(c *gin.Context) {
		guessStr := c.PostForm("guess")
		guess, err := strconv.Atoi(guessStr)
		if err != nil {
			logger.Println("Invalid input received during guess")
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

		logger.Printf("User guessed: %d, Response: %s", guess, feedback)
		c.HTML(http.StatusOK, "index", gin.H{"Feedback": feedback})
	})

	return r
}

func resetSecretNumber() {
	secretNumber = rng.Intn(100) + 1
	logger.Println("Reset secret number")
}
