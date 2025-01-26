package handlers

import (
	"fmt"
	"io"
	"math/rand/v2"
	"net/http"
	"os"

	"github.com/gofiber/fiber/v2"
)

// NewRoot creates a handler for the root page returning fact about random number.
func NewRoot() func(*fiber.Ctx) error {
	file := "./static/index.html"
	content, err := os.ReadFile(file)
	if err != nil {
		panic("can not open static content")
	}

	template := string(content)
	return func(c *fiber.Ctx) error {
		const maxRandomNumber = 2024
		num := rand.IntN(maxRandomNumber)

		return c.Type("html").SendString(fmt.Sprintf(template, getNumberFact(num)))
	}
}

// getNumberFact uses numbersapi to return fact about given number.
func getNumberFact(num int) string {
	const api = "http://numbersapi.com/%d"
	const noAnswer = "Unfortunately, no fact for today :("

	resp, err := http.Get(fmt.Sprintf(api, num))
	if err != nil {
		return noAnswer
	}

	fact, err := io.ReadAll(resp.Body)
	if err != nil {
		return noAnswer
	}
	return string(fact)
}
