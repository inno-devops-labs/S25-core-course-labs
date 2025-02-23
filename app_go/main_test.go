package main

import (
    "net/http"
    "net/http/httptest"
    "testing"
    "time"
)

func TestMoscowTimeEndpoint(t *testing.T) {
    router := gin.Default()
    router.GET("/", func(c *gin.Context) {
        moscowTime := time.Now().UTC().Add(3 * time.Hour).Format("2006-01-02 15:04:05")
        c.String(http.StatusOK, fmt.Sprintf("Current time in Moscow: %s", moscowTime))
    })

    req, err := http.NewRequest("GET", "/", nil)
    if err != nil {
        t.Fatalf("Failed to create request: %v", err)
    }

    resp := httptest.NewRecorder()
    router.ServeHTTP(resp, req)

    if resp.Code != http.StatusOK {
        t.Errorf("Expected status code %d, got %d", http.StatusOK, resp.Code)
    }

    expectedPrefix := "Current time in Moscow: "
    if !strings.HasPrefix(resp.Body.String(), expectedPrefix) {
        t.Errorf("Expected response to start with '%s', got '%s'", expectedPrefix, resp.Body.String())
    }
}