package main

import (
	"encoding/json"
	"html/template"
	"log"
	"net/http"
	"time"
)

// API response structure
type TimeAPIResponse struct {
	DateTime string `json:"dateTime"`
}

// handler for the homepage
func homeHandler(w http.ResponseWriter, r *http.Request) {
	// API URL
	timeAPIURL := "https://timeapi.io/api/Time/current/zone?timeZone=Europe/Moscow"

	// HTTP client with timeout (5 seconds)
	client := http.Client{Timeout: 5 * time.Second}
	resp, err := client.Get(timeAPIURL)
	if err != nil {
		http.Error(w, "failed to fetch time: " + err.Error(), http.StatusInternalServerError)
		return
	}
	defer resp.Body.Close()

	// parse JSON response
	var timeData TimeAPIResponse
	if err := json.NewDecoder(resp.Body).Decode(&timeData); err != nil {
		http.Error(w, "failed to parse time response", http.StatusInternalServerError)
		return
	}

	// format the time string
	formattedTime := timeData.DateTime
	if len(formattedTime) > 0 {
		formattedTime = formattedTime[:19] // keep only YYYY-MM-DD HH:MM:SS
	}

	// render the template and execute it with the formatted time
	tmpl, err := template.ParseFiles("index.html")
	if err != nil {
		http.Error(w, "error loading template", http.StatusInternalServerError)
		return
	}
	tmpl.Execute(w, map[string]string{"Time": formattedTime})
}

func main() {
	http.HandleFunc("/", homeHandler)
	log.Println("Server started on :8000")
	log.Fatal(http.ListenAndServe(":8000", nil))
}
