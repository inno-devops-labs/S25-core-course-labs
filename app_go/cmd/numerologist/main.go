// Package numerologist provides application generating facts abound random numbers.
package main

import (
	"log"

	"github.com/m0t9/S25-core-course-labs/app_go/internal/server"
)

func main() {
	app := server.New()

	if err := app.Listen(":8080"); err != nil {
		log.Fatal(err)
	}
}
