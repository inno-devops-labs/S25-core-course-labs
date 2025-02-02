package main

import (
	"net/http"
	"net/http/httptest"
	"regexp"
	"strconv"
	"testing"
)

// Server performance testing
func TestServerIsUp(t *testing.T) {
	handl := http.HandlerFunc(handleTime)
	serv := httptest.NewServer((handl))

	response, err := http.Get(serv.URL)
	if err != nil {
		t.Fatal((err))
	}

	if response.StatusCode != http.StatusOK {
		t.Errorf("Server status error: %v", response.Status)
	}
}

// Testing random number display 
func TestNumber(t *testing.T) {
	request, err := http.NewRequest("GET", "/", nil)
	if err != nil {
		t.Fatal("Request error :", err)
	}

	new_record := httptest.NewRecorder()
	handler := http.HandlerFunc(handleTime)
	handler.ServeHTTP(new_record, request)

	body := new_record.Body.String()
	re := regexp.MustCompile(`>\s*(\d+)\s*<`)
	match := re.FindStringSubmatch(body)
	if len(match) < 2 {
		t.Fatalf("Not find a number: %v", body)
	}
	number_str := match[1]

    number, _ := strconv.Atoi(number_str)

	if number < 0 || number > 100 {
		t.Errorf("number less than 0 or greater than 100 %d", number)
	}
}