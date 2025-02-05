package main

import (
	"encoding/json"
	"net/http"
	"net/http/httptest"
	"testing"
	"time"
)

func TestHandler(t *testing.T) {
	req, err := http.NewRequest("GET", "/", nil)
	if err != nil {
		t.Fatal(err)
	}

	rr := httptest.NewRecorder()
	handler(rr, req)

	if status := rr.Code; status != http.StatusOK {
		t.Errorf("handler returned wrong status code: got %v want %v", status, http.StatusOK)
	}

	var response map[string]string
	err = json.Unmarshal(rr.Body.Bytes(), &response)
	if err != nil {
		t.Fatal("Failed to parse JSON response")
	}

	moscowTimeStr, exists := response["moscow_time"]
	if !exists {
		t.Fatal("moscow_time key not found in response")
	}

	parsedTime, err := time.Parse(time.RFC3339, moscowTimeStr)
	if err != nil {
		t.Fatal("moscow_time is not in a valid format")
	}

	moscowLocation, _ := time.LoadLocation("Europe/Moscow")
	currentTime := time.Now().In(moscowLocation)

	timeDiff := currentTime.Sub(parsedTime).Seconds()
	if timeDiff < 0 {
		timeDiff = -timeDiff
	}

	if timeDiff > 2 {
		t.Errorf("Time difference is too large: got %v, expected within 2 seconds", timeDiff)
	}
}
