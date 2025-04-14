package main

import (
	"io/ioutil"
	"net/http"
	"testing"
)

func TestServerResponse(t *testing.T) {
	resp, err := http.Get("http://127.0.0.1:8080/")
	if err != nil {
		t.Fatalf("Failed to send request: %v", err)
	}
	defer resp.Body.Close()

	body, _ := ioutil.ReadAll(resp.Body)
	if resp.StatusCode != 200 || !contains(string(body), "Current Time in Moscow") {
		t.Errorf("Unexpected response: %s", body)
	}
}

func contains(str, substr string) bool {
	return len(str) >= len(substr) && (str == substr || contains(str[1:], substr))
}