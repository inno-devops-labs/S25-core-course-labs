package main

import (
	"net/http"
	"net/http/httptest"
	"strings"
	"testing"
)

func setupTestQuotes() {
	quotes = []string{
		"Programs must be written for people to read, and only incidentally for machines to execute. – Harold Abelson",
		"Any fool can write code that a computer can understand. Good programmers write code that humans can understand. – Martin Fowler",
		"First, solve the problem. Then, write the code. – John Johnson",
		"Experience is the name everyone gives to their mistakes. – Oscar Wilde",
		"Java is to JavaScript what car is to Carpet. – Chris Heilmann",
		"Knowledge is power. – Francis Bacon",
		"Your body is like a piece of dynamite. You can tap it with a pencil all day, but you'll never make it explode. You hit it once with a hammer: Bang! Get serious. Do 40 hard minutes, not an hour and half of nonsense. It's so much more rewarding. - Jason Statham",
	}
}

// Test if the homepage returns a 200 OK status
func TestHomepageStatus(t *testing.T) {
	setupTestQuotes()

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
