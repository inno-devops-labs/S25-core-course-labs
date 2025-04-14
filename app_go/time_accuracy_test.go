package main

import (
	"net/http"
	"net/http/httptest"
	"strings"
	"testing"
	"time"
)

// Test for checking the accuracy of the current time in Moscow.
func TestCurrentTimeAccuracy(t *testing.T) {
	// Get the current time in Moscow
	location, err := time.LoadLocation("Europe/Moscow")
	if err != nil {
		t.Fatal(err)
	}
	currentTime := time.Now().In(location)
	formattedTime := currentTime.Format("15:04:05")

	// Fetch the time from the home route
	req, err := http.NewRequest("GET", "/", nil)
	if err != nil {
		t.Fatal(err)
	}
	rr := httptest.NewRecorder()
	handler := http.HandlerFunc(Home)
	handler.ServeHTTP(rr, req)

	// Check if the time returned in the response is close to the actual current time in Moscow
	if !strings.Contains(rr.Body.String(), formattedTime) {
		t.Errorf("Expected current time to be around %s, but got different time.", formattedTime)
	}
}
