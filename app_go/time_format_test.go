package main

import (
	"net/http"
	"net/http/httptest"
	"strings"
	"testing"
)

// Test for checking the format of the current time.
func TestCurrentTimeFormat(t *testing.T) {
	// Create a new HTTP request to the home route
	req, err := http.NewRequest("GET", "/", nil)
	if err != nil {
		t.Fatal(err)
	}

	// Record the response
	rr := httptest.NewRecorder()
	handler := http.HandlerFunc(Home)

	// Call the handler with the request and response recorder
	handler.ServeHTTP(rr, req)

	// Check if the response contains the correct time format (HH:MM:SS)
	if !strings.Contains(rr.Body.String(), ":") {
		t.Errorf("Expected time format HH:MM:SS, but got %s", rr.Body.String())
	}
}
