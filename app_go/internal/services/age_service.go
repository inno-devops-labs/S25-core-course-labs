package services

import (
	"errors"
	"time"
)

func CalculateAge(date string) (int, error) {
	const layout = "2006-01-02"
	parsedDob, err := time.Parse(layout, date)
	if err != nil {
		println(err.Error())
		return -1, errors.New("Invalid date format. Use YYYY-MM-DD")
	}

	now := time.Now()
	age := now.Year() - parsedDob.Year()
	if now.YearDay() < parsedDob.YearDay() {
		age--
	}

	if age < 0 {
		return -1, errors.New("Negative age")
	}

	return age, nil
}
