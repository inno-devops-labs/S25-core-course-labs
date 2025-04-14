package main

import (
	"encoding/json"
	"io/ioutil"
	"net/http"
	"time"
)

const (
	// Port to run the application
	appPort = ":8002"

	// Date format to display
	dateFormat = "2006-01-02"

	// Timezone to display the date
	timezone = "Europe/Moscow"

	// HTML file with the web page
	HTMLFileName = "index.html"
)

// Response model with a date field
type DateResponse struct {
	Date string `json:"date"`
}

// Returns the HTML web page that displays the current date
// in the specified timezone using API
func getCurrentDateHTML(w http.ResponseWriter, r *http.Request) {
	htmlContent, err := ioutil.ReadFile(HTMLFileName)

	if err != nil {
		http.Error(w, "Internal Server Error", http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "text/html")
	w.Write(htmlContent)
}

// Returns the current date in the specified timezone
func getCurrentDate(w http.ResponseWriter, r *http.Request) {
	location, err := time.LoadLocation(timezone)

	if err != nil {
		http.Error(w, "Internal Server Error", http.StatusInternalServerError)
		return
	}

	response := DateResponse{Date: time.Now().In(location).Format(dateFormat)}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(response)
}

func main() {
	http.HandleFunc("/", getCurrentDateHTML)
	http.HandleFunc("/api/date", getCurrentDate)

	http.ListenAndServe(appPort, nil)
}
