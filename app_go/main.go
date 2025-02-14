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

func main() {
	r := gin.Default()

	rand.Seed(time.Now().UnixNano())
	resetSecretNumber()

	r.SetHTMLTemplate(template.Must(template.New("index").Parse(`
		<!DOCTYPE html>
		<html lang="en">
		<head>
			<meta charset="UTF-8">
			<meta name="viewport" content="width=device-width, initial-scale=1.0">
			<title>Guess the Number</title>
			<style>
				body {
					font-family: Arial, sans-serif;
					text-align: center;
					margin-top: 10%;
					background-color: #f5f5f5;
					color: #333;
				}
				h1 {
					font-size: 2rem;
					margin-bottom: 1rem;
				}
				p {
					font-size: 1.2rem;
				}
				form {
					margin-top: 1rem;
				}
				input[type="number"] {
					padding: 0.5rem;
					font-size: 1rem;
				}
				button {
					padding: 0.5rem 1rem;
					font-size: 1rem;
					margin-left: 1rem;
					cursor: pointer;
				}
			</style>
		</head>
		<body>
			<h1>Guess the Number</h1>
			<p>I have picked a random number between 1 and 100. Can you guess it?</p>
			{{if .Feedback}}
				<p><strong>{{.Feedback}}</strong></p>
			{{end}}
			<form method="POST" action="/">
				<input type="number" name="guess" placeholder="Enter your guess" required>
				<button type="submit">Guess</button>
			</form>
		</body>
		</html>
	`)))

	r.GET("/", func(c *gin.Context) {
		c.HTML(http.StatusOK, "index", gin.H{
			"Feedback": nil,
		})
	})

	r.POST("/", func(c *gin.Context) {
		guessStr := c.PostForm("guess")
		guess, err := strconv.Atoi(guessStr)
		if err != nil {
			c.HTML(http.StatusBadRequest, "index", gin.H{
				"Feedback": "Invalid input. Please enter a number.",
			})
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

		c.HTML(http.StatusOK, "index", gin.H{
			"Feedback": feedback,
		})
	})

	r.Run(":8080")
}

func resetSecretNumber() {
	secretNumber = rand.Intn(100) + 1
}
