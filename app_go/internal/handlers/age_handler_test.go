package handlers_test

import (
	"bytes"
	"net/http"
	"net/http/httptest"
	"testing"

	"app_go/internal/handlers"

	"github.com/gin-gonic/gin"
)

func TestRenderIndex(t *testing.T) {
	gin.SetMode(gin.TestMode)

	router := gin.Default()
	router.LoadHTMLGlob("../templates/index.html")

	router.GET("/", handlers.RenderIndex)

	req, err := http.NewRequest("GET", "/", nil)
	if err != nil {
		t.Errorf("Failed to create request: %v", err)
	}

	resp := httptest.NewRecorder()
	router.ServeHTTP(resp, req)

	if resp.Code != http.StatusOK {
		t.Errorf("Expected status code %d, got %d", http.StatusOK, resp.Code)
	}

	expectedContentType := "text/html; charset=utf-8"
	if contentType := resp.Header().Get("Content-Type"); contentType != expectedContentType {
		t.Errorf("Expected Content-Type '%s', got '%s'", expectedContentType, contentType)
	}
}

func TestCalculateAge_ValidDate(t *testing.T) {
	gin.SetMode(gin.TestMode)

	router := gin.Default()
	router.GET("/calculate-age", handlers.CalculateAge)

	req, err := http.NewRequest("GET", "/calculate-age?date=2004-08-10", nil)
	if err != nil {
		t.Errorf("Failed to create request: %v", err)
	}

	resp := httptest.NewRecorder()
	router.ServeHTTP(resp, req)

	if resp.Code != http.StatusOK {
		t.Errorf("Expected status code %d, got %d", http.StatusOK, resp.Code)
	}

	expectedBody := `{"age":`
	if !bytes.Contains(resp.Body.Bytes(), []byte(expectedBody)) {
		t.Errorf("Expected response body to contain '%s', got '%s'", expectedBody, resp.Body.String())
	}
}

func TestCalculateAge_InvalidDate(t *testing.T) {
	gin.SetMode(gin.TestMode)

	router := gin.Default()
	router.GET("/calculate-age", handlers.CalculateAge)

	req, err := http.NewRequest("GET", "/calculate-age?date=creed", nil)
	if err != nil {
		t.Errorf("Failed to create request: %v", err)
	}

	resp := httptest.NewRecorder()
	router.ServeHTTP(resp, req)

	if resp.Code != http.StatusBadRequest {
		t.Errorf("Expected status code %d, got %d", http.StatusBadRequest, resp.Code)
	}

	expectedBody := `{"error":"Invalid date format. Use YYYY-MM-DD"}`
	if !bytes.Contains(resp.Body.Bytes(), []byte(expectedBody)) {
		t.Errorf("Expected response body to contain '%s', got '%s'", expectedBody, resp.Body.String())
	}
}
