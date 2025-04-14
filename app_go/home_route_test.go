package main

import (
	"net/http"
	"net/http/httptest"
	"testing"
)

// Test for checking if the home route is accessible.
func TestHomeRouteExists(t *testing.T) {
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

	// Check the status code to ensure the home route is accessible (200 OK)
	if status := rr.Code; status != http.StatusOK {
		t.Errorf("Expected status code 200, got %v", status)
	}
}
