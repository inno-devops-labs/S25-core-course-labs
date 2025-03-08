package services

import (
	"os"
	"strconv"
	"sync"
)

var mu sync.Mutex

const visitsFilePath = "visits/visits.txt"

func IncrementVisits() (int, error) {
	mu.Lock()
	defer mu.Unlock()

	var count int
	data, err := os.ReadFile(visitsFilePath)
	if err != nil {
		return 0, err
	} else {
		count, err = strconv.Atoi(string(data))
		if err != nil {
			return 0, err
		}
	}

	count++

	err = os.WriteFile(visitsFilePath, []byte(strconv.Itoa(count)), 0644)
	if err != nil {
		return 0, err
	}
	return count, nil
}

func ReadVisits() (int, error) {
	mu.Lock()
	defer mu.Unlock()

	var count int
	data, err := os.ReadFile(visitsFilePath)
	if err != nil {
		return 0, err
	} else {
		count, err = strconv.Atoi(string(data))
		if err != nil {
			return 0, err
		}
	}
	return count, nil
}
