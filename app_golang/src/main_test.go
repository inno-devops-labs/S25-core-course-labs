package main

import (
	"net/http"
	"net/http/httptest"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestJokeJson(t *testing.T) {
	router := setupRouter(false)

	w := httptest.NewRecorder()
	req, _ := http.NewRequest("GET", "/joke", nil)
	router.ServeHTTP(w, req)
	
	assert.Equal(t, 200, w.Code)
	assert.Greater(t, len(w.Body.String()), 0)
}

func TestJoke(t *testing.T) {
	router := setupRouter(false)

	w := httptest.NewRecorder()
	req, _ := http.NewRequest("GET", "/", nil)
	router.ServeHTTP(w, req)

	assert.Equal(t, 200, w.Code)
	assert.Greater(t, len(w.Body.String()), 0)	
}