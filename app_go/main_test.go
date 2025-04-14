package main

import (
	"encoding/json"
	"net/http"
	"net/http/httptest"
	"testing"
)

func TestGreetHandler(t *testing.T) {
	tests := []struct {
		endpoint         string
		expectedGreeting string
	}{
		{
			endpoint:         "/greet?name=John",
			expectedGreeting: "Hello, John! Welcome!",
		},
		{
			endpoint:         "/greet",
			expectedGreeting: "Hello, Guest! Welcome!",
		},
	}

	for _, test := range tests {
		// Create a request to pass to the handler
		req := httptest.NewRequest("GET", test.endpoint, nil)
		respRecorder := httptest.NewRecorder()

		// Call the handler
		greetHandler(respRecorder, req)

		// Verify the status code
		if status := respRecorder.Code; status != http.StatusOK {
			t.Fatalf("Handler returned wrong status code: got %v want %v", status, http.StatusOK)
		}

		// Parse the response body
		var response GreetingResponse
		err := json.NewDecoder(respRecorder.Body).Decode(&response)
		if err != nil {
			t.Fatalf("Unable to parse response JSON: %v", err)
		}

		// Verify the response content
		if response.Greeting != test.expectedGreeting {
			t.Errorf("Handler returned unexpected body: got %v want %v", response.Greeting, test.expectedGreeting)
		}

	}
}
