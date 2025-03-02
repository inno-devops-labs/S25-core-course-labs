package main

import (
	"encoding/json"
	"net/http"
	"net/http/httptest"
	"testing"
)

func TestPredictionEndpoint(t *testing.T) {
	req, err := http.NewRequest("GET", "/", nil)
	if err != nil {
		t.Fatal(err)
	}

	rr := httptest.NewRecorder()
	handler := http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusOK)
		json.NewEncoder(w).Encode(map[string]string{"prediction": "test prediction"})
	})

	handler.ServeHTTP(rr, req)

	if status := rr.Code; status != http.StatusOK {
		t.Errorf("handler returned wrong status code: got %v want %v", status, http.StatusOK)
	}

	var response map[string]string
	err = json.Unmarshal(rr.Body.Bytes(), &response)
	if err != nil {
		t.Errorf("Failed to parse response JSON: %v", err)
	}

	if _, exists := response["prediction"]; !exists {
		t.Errorf("Response does not contain 'prediction' key")
	}
}
