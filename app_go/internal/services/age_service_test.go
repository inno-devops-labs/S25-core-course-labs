package services_test

import (
	"testing"
	"time"

	"app_go/internal/services"
)

func TestCalculateAge_ValidDate(t *testing.T) {
	date := "2004-08-10"
	correctAge := time.Now().Year() - 2004
	if time.Now().YearDay() < time.Date(2004, 8, 10, 0, 0, 0, 0, time.UTC).YearDay() {
		correctAge--
	}

	age, err := services.CalculateAge(date)
	if err != nil {
		t.Errorf("Expected no error, got %v", err)
	}
	if age != correctAge {
		t.Errorf("Expected age %d, got %d", correctAge, age)
	}
}

func TestCalculateAge_InvalidDateFormat(t *testing.T) {
	date := "10-08-2000"
	_, err := services.CalculateAge(date)
	if err == nil || err.Error() != "Invalid date format. Use YYYY-MM-DD" {
		t.Errorf("Expected error 'Invalid date format. Use YYYY-MM-DD', got %v", err)
	}
}

func TestCalculateAge_NegativeAge(t *testing.T) {
	date := "2104-11-10"
	_, err := services.CalculateAge(date)
	if err == nil || err.Error() != "Negative age" {
		t.Errorf("Expected error 'Negative age', got %v", err)
	}
}

func TestCalculateAge_EmptyDate(t *testing.T) {
	date := ""
	_, err := services.CalculateAge(date)
	if err == nil || err.Error() != "Invalid date format. Use YYYY-MM-DD" {
		t.Errorf("Expected error 'Invalid date format. Use YYYY-MM-DD', got %v", err)
	}
}
