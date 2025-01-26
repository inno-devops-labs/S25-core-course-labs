// Package server provides functions to build the fiber server.
package server

import (
	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/fiber/v2/middleware/logger"

	"github.com/m0t9/S25-core-course-labs/app_go/internal/handlers"
)

// New creates a fiber application returning a fact about random number.
func New(cfgs ...fiber.Config) *fiber.App {
	s := fiber.New(cfgs...)

	// Enable logging.
	s.Use(logger.New())

	// Register handlers.
	handlers.RegisterAll(s)

	return s
}
