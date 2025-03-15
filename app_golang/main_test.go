package main

import (
	"encoding/json"
	"net/http"
	"net/http/httptest"
	"testing"
	"time"

	"github.com/gin-gonic/gin"
	"github.com/stretchr/testify/assert"
)

func TestTimeEndpoint(t *testing.T) {
	gin.SetMode(gin.TestMode)
	location, err := time.LoadLocation("Europe/Moscow")
	if err != nil {
		t.Fatalf("Failed to load location: %v", err)
	}
	router := gin.Default()
	router.GET("/time", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"time": time.Now().In(location),
		})
	})

	req, err := http.NewRequest(http.MethodGet, "/time", nil)
	if err != nil {
		t.Fatalf("Could not create HTTP request: %v", err)
	}

	recorder := httptest.NewRecorder()
	router.ServeHTTP(recorder, req)

	assert.Equal(t, http.StatusOK, recorder.Code)

	var response map[string]interface{}
	err = json.Unmarshal(recorder.Body.Bytes(), &response)
	if err != nil {
		t.Fatalf("Failed to parse JSON response: %v", err)
	}

	assert.Contains(t, response, "time")

	_, parseErr := time.Parse(time.RFC3339, response["time"].(string))
	assert.NoError(t, parseErr, "The time field is not in a valid format")
}
