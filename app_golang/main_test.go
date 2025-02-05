package main

import (
	"log"
	"net/http"
	"net/http/httptest"
	"os"
	"strings"
	"testing"
)

func setupTestQuotes() {
	file, err := os.ReadFile("app_golang/quotes.txt")
	if err != nil {
		log.Fatalf("Failed to read quotes file: %v", err)
	}
	quotes = strings.Split(strings.TrimSpace(string(file)), "\n")
}

// Test if the homepage returns a 200 OK status
func TestHomepageStatus(t *testing.T) {

	req, err := http.NewRequest("GET", "/", nil)
	if err != nil {
		t.Fatal(err)
	}

	recorder := httptest.NewRecorder()
	handler := http.HandlerFunc(randomQuoteHandler)

	handler.ServeHTTP(recorder, req)

	if status := recorder.Code; status != http.StatusOK {
		t.Errorf("Expected status code %d, got %d", http.StatusOK, status)
	}
}

// Test if the response contains a quote
func TestQuoteInResponse(t *testing.T) {
	setupTestQuotes()

	req, err := http.NewRequest("GET", "/", nil)
	if err != nil {
		t.Fatal(err)
	}

	recorder := httptest.NewRecorder()
	handler := http.HandlerFunc(randomQuoteHandler)

	handler.ServeHTTP(recorder, req)

	responseBody := recorder.Body.String()
	found := false

	for _, quote := range quotes {
		if strings.Contains(responseBody, quote) {
			found = true
			break
		}
	}

	if !found {
		t.Errorf("Response does not contain any expected quotes")
	}
}
