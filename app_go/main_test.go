package main

import (
	"net/http"
	"net/http/httptest"
	"net/url"
	"strconv"
	"strings"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestHomePage(t *testing.T) {
	r := setupRouter()
	w := httptest.NewRecorder()
	req, _ := http.NewRequest("GET", "/", nil)
	r.ServeHTTP(w, req)

	assert.Equal(t, http.StatusOK, w.Code)
	assert.Contains(t, w.Body.String(), "<body>")
}

func TestInvalidInput(t *testing.T) {
	r := setupRouter()
	w := httptest.NewRecorder()

	form := url.Values{}
	form.Add("guess", "invalid")
	req, _ := http.NewRequest("POST", "/", strings.NewReader(form.Encode()))
	req.Header.Set("Content-Type", "application/x-www-form-urlencoded")
	r.ServeHTTP(w, req)

	assert.Equal(t, http.StatusBadRequest, w.Code)
	assert.Contains(t, w.Body.String(), "Invalid input. Please enter a number.")
}

func TestGuessNumber(t *testing.T) {
	r := setupRouter()
	secretNumber = 50

	cases := []struct {
		guess  int
		expect string
	}{
		{40, "Too Low!"},
		{60, "Too High!"},
		{50, "Correct! You guessed the number!"},
	}

	for _, tc := range cases {
		w := httptest.NewRecorder()
		form := url.Values{}
		form.Add("guess", strconv.Itoa(tc.guess))
		req, _ := http.NewRequest("POST", "/", strings.NewReader(form.Encode()))
		req.Header.Set("Content-Type", "application/x-www-form-urlencoded")
		r.ServeHTTP(w, req)

		assert.Equal(t, http.StatusOK, w.Code)
		assert.Contains(t, w.Body.String(), tc.expect)
	}
}

func TestSecretNumberReset(t *testing.T) {
	r := setupRouter()
	secretNumber = 25

	w := httptest.NewRecorder()
	form := url.Values{}
	form.Add("guess", "25")
	req, _ := http.NewRequest("POST", "/", strings.NewReader(form.Encode()))
	req.Header.Set("Content-Type", "application/x-www-form-urlencoded")

	r.ServeHTTP(w, req)
	assert.Contains(t, w.Body.String(), "Correct! You guessed the number!")

	oldSecret := secretNumber
	resetSecretNumber()
	assert.NotEqual(t, oldSecret, secretNumber)
}
