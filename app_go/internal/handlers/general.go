// Package handlers is used for all the projects handlers storing and tools for them.
package handlers

import "github.com/gofiber/fiber/v2"

// RegisterAll function registers all the handlers to app.
func RegisterAll(s *fiber.App) {
	s.Get("/", NewRoot())
}
