package main

import (
	"net/http"
	"net/http/httptest"
	"regexp"
	"testing"
	"time"
)

// Test timePassedSince function
func TestTimePassedSince(t *testing.T) {
	testDate := time.Date(2000, time.January, 1, 0, 0, 0, 0, time.UTC)
	years, months, days := timePassedSince(testDate)

	if years < 24 || months < 0 || days < 0 {
		t.Errorf("Unexpected result: %d years, %d months, %d days", years, months, days)
	}
}

func TestHandler(t *testing.T) {
	req := httptest.NewRequest("GET", "/", nil)
	rec := httptest.NewRecorder()

	handler(rec, req)

	res := rec.Result()
	defer res.Body.Close()

	if res.StatusCode != http.StatusOK {
		t.Errorf("Expected status OK, got %v", res.Status)
	}
}

// Test regex extraction from header
func TestRegexExtraction(t *testing.T) {
	header := `<https://api.github.com/repos/torvalds/linux/commits?sha=master&per_page=1&page=1000>; rel="last"`
	number := extractCommitNumber(header)

	if number != "1000" {
		t.Errorf("Expected 1000, got %s", number)
	}
}

// Helper function for regex
func extractCommitNumber(linkHeader string) string {
	re := regexp.MustCompile(`page=(\d+)>;`)
	matches := re.FindStringSubmatch(linkHeader)
	if len(matches) > 1 {
		return matches[1]
	}
	return "0"
}
