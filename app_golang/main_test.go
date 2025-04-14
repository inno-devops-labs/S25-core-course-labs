package main

import (
	"net/http"
	"net/http/httptest"
	"testing"
)

func TestGetMoscowTime(t *testing.T) {
	req, err := http.NewRequest("GET", "/msc_time", nil)
	if err != nil {
		t.Fatal(err)
	}

	rr := httptest.NewRecorder()

	handler := http.HandlerFunc(GetMoscowTime)
	handler.ServeHTTP(rr, req)

	if status := rr.Code; status != http.StatusOK {
		t.Errorf("Expected status 200 OK, got %v", status)
	}
}
