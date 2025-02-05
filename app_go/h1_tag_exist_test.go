package main

import (
	"net/http"
	"net/http/httptest"
	"strings"
	"testing"
)

// Test for checking if the <h1> tag exists in the response.
func TestH1TagExists(t *testing.T) {
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

	// Check if the <h1> tag exists in the response body
	if !strings.Contains(rr.Body.String(), "<h1>") {
		t.Errorf("Expected <h1> tag to exist, but it was not found.")
	}
}
