// Package server provides functions to build the fiber server.
package server

import (
	"github.com/ansrivas/fiberprometheus/v2"
	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/fiber/v2/middleware/logger"

	"github.com/m0t9/S25-core-course-labs/app_go/internal/handlers"
)

// New creates a fiber application returning a fact about random number.
func New(withVisits bool, cfgs ...fiber.Config) *fiber.App {
	s := fiber.New(cfgs...)
	handlers.WithVisits = withVisits

	// Enable logging.
	s.Use(logger.New())

	// Enable metrics collection.
	prom := fiberprometheus.New("app_go")
	prom.RegisterAt(s, "/metrics")
	s.Use(prom.Middleware)

	// Register handlers.
	handlers.RegisterAll(s)

	return s
}
