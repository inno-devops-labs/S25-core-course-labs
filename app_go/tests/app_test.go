package main

import (
	"fmt"
	"net/http"
	"net/http/httptest"
	"testing"
	"time"
)

func innoTimeHandler(w http.ResponseWriter, r *http.Request) {
	loc, err := time.LoadLocation("Europe/Moscow")
	if err != nil {
		http.Error(w, "Error loading time zone", http.StatusInternalServerError)
		return
	}
	currentTime := time.Now().In(loc).Format("2006-01-02 15:04:05")
	fmt.Fprintf(w, "<h1>Current time in Innopolis: %s</h1>", currentTime)
}

func TestHomeHandler(t *testing.T) {
	req, err := http.NewRequest("GET", "/", nil)
	if err != nil {
		t.Fatal(err)
	}

	rr := httptest.NewRecorder()
	handler := http.HandlerFunc(innoTimeHandler)
	handler.ServeHTTP(rr, req)

	if status := rr.Code; status != http.StatusOK {
		t.Errorf("Expecting %d, get %d", http.StatusOK, status)
	}
}

func TestHomeHandlerResponse(t *testing.T) {
	req, err := http.NewRequest("GET", "/", nil)
	if err != nil {
		t.Fatal(err)
	}

	rr := httptest.NewRecorder()
	handler := http.HandlerFunc(innoTimeHandler)

	handler.ServeHTTP(rr, req)

	expected := "Current time in Innopolis\n"
	if rr.Body.String() != expected {
		t.Errorf("Expecting '%s', get '%s'", expected, rr.Body.String())
	}
}
