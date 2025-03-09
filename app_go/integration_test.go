package main

import (
	"io"
	"net/http"
	"strings"
	"testing"
	"time"
)

func TestMainServerIntegration(t *testing.T) {
	go func() {
		main()
	}()

	time.Sleep(1 * time.Second)

	resp, err := http.Get("http://localhost:8080")
	if err != nil {
		t.Fatalf("Failed to get response from server: %v", err)
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		t.Fatalf("Expected HTTP status 200, got %d", resp.StatusCode)
	}
	body, err := io.ReadAll(resp.Body)
	if err != nil {
		t.Fatalf("Failed to read response body: %v", err)
	}

	expectedSubstring := "Loading. Please wait"
	if !strings.Contains(string(body), expectedSubstring) {
		t.Errorf("Expected response body to contain %q, got %q", expectedSubstring, string(body))
	}
}
