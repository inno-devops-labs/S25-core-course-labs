package main

import (
	"encoding/json"
	"net/http"
	"net/http/httptest"
	"testing"
	"time"
)

func TestGetCurrentDate(t *testing.T) {
	req, err := http.NewRequest("GET", "/api/date", nil)
	if err != nil {
		t.Fatalf("Failed to create request: %v", err)
	}

	recorder := httptest.NewRecorder()
	handler := http.HandlerFunc(getCurrentDate)
	handler.ServeHTTP(recorder, req)

	if status := recorder.Code; status != http.StatusOK {
		t.Errorf("Handler returned wrong status code: got %v want %v", status, http.StatusOK)
	}

	var response DateResponse
	if err := json.Unmarshal(recorder.Body.Bytes(), &response); err != nil {
		t.Fatalf("Failed to parse response JSON: %v", err)
	}

	location, _ := time.LoadLocation(timezone)
	expectedDate := time.Now().In(location).Format(dateFormat)

	if response.Date != expectedDate {
		t.Errorf("Unexpected date: got %v want %v", response.Date, expectedDate)
	}
}

func TestGetCurrentDateHTML(t *testing.T) {
	req, err := http.NewRequest("GET", "/", nil)
	if err != nil {
		t.Fatalf("Failed to create request: %v", err)
	}

	recorder := httptest.NewRecorder()
	handler := http.HandlerFunc(getCurrentDateHTML)
	handler.ServeHTTP(recorder, req)

	if status := recorder.Code; status != http.StatusOK {
		t.Errorf("Handler returned wrong status code: got %v want %v", status, http.StatusOK)
	}

	if contentType := recorder.Header().Get("Content-Type"); contentType != "text/html" {
		t.Errorf("Wrong Content-Type header: got %v want %v", contentType, "text/html")
	}
}
