package main

import (
	"net/http"
	"net/http/httptest"
	"strings"
	"testing"
	"time"
)

func TestStatusCode(t *testing.T) {
	req, err := http.NewRequest("GET", "/", nil)
	if err != nil {
		t.Fatal(err)
	}

	rr := httptest.NewRecorder()
	handler := http.HandlerFunc(getMoscowTime)

	handler.ServeHTTP(rr, req)

	if status := rr.Code; status != http.StatusOK {
		t.Fatalf("Unexpected status code. Expected %v, but got %v", http.StatusOK, status)
	}
}

func TestAccuracy(t *testing.T) {
	req, err := http.NewRequest("GET", "/", nil)
	if err != nil {
		t.Fatal(err)
	}

	rr := httptest.NewRecorder()
	handler := http.HandlerFunc(getMoscowTime)

	handler.ServeHTTP(rr, req)

	// Extract the time from the response
	responseBody := rr.Body.String()
	responseTimeStr := responseBody[strings.Index(responseBody, "Time in Moscow - ")+len("Time in Moscow - "):]
	responseTimeStr = responseTimeStr[:strings.Index(responseTimeStr, "<")]
	responseTime, err := time.Parse("15:04:05", responseTimeStr)
	if err != nil {
		t.Fatal(err)
	}

	// Get the current time in Moscow
	loc, err := time.LoadLocation("Europe/Moscow")
	if err != nil {
		t.Fatal(err)
	}
	currentTime := time.Now().In(loc)

	// Convert times to seconds
	responseTimeInSeconds := responseTime.Hour()*3600 + responseTime.Minute()*60 + responseTime.Second()
	currentTimeInSeconds := currentTime.Hour()*3600 + currentTime.Minute()*60 + currentTime.Second()

	// Allow for a 10-second inaccuracy
	allowedInaccuracy := 10
	if abs(responseTimeInSeconds-currentTimeInSeconds) > allowedInaccuracy {
		t.Fatalf("Response time is not accurate!")
	}
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
