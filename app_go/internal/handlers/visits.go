package handlers

import (
	"fmt"
	"os"
	"strconv"

	"github.com/gofiber/fiber/v2"
)

const visitsFile = "/data/visits.txt"

func getVisitCount() (int, error) {
	prepareFile()
	data, err := os.ReadFile(visitsFile)
	if err != nil {
		return 0, err
	}
	count, err := strconv.Atoi(string(data))
	if err != nil {
		return 0, err
	}
	return count, nil
}

func prepareFile() {
	if _, err := os.Stat(visitsFile); os.IsNotExist(err) {
		err := os.WriteFile(visitsFile, []byte("0"), 0644)
		if err != nil {
			panic(fmt.Sprintf("Failed to create visits file: %v", err))
		}
	}

}

func incrementVisitCount() error {
	prepareFile()
	count, err := getVisitCount()
	if err != nil {
		return err
	}

	count++
	err = os.WriteFile(visitsFile, []byte(strconv.Itoa(count)), 0644)
	return err
}

func NewVisits() func(*fiber.Ctx) error {
	return func(c *fiber.Ctx) error {
		visitsCnt, err := getVisitCount()
		if err != nil {
			return err
		}
		return c.JSON(map[string]any{
			"visits": visitsCnt,
		})
	}
}
