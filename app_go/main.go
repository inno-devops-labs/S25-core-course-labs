package main

import (
	"encoding/json"
	"io/ioutil"
	"log"
	"net/http"
	"os"
	"path/filepath"
	"strconv"
	"strings"
	"sync"
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

	// Folder to store the number of visits
	visitsFolderName = "visits"

	// File with the number of visits
	visitsFileName = "visits-go.txt"
)

var mu sync.Mutex

func incrementVisits() (int, error) {
	mu.Lock()
	defer mu.Unlock()

	// Ensure the visits folder exists
	if err := os.MkdirAll(visitsFolderName, os.ModePerm); err != nil {
		return 0, err
	}

	visitsFilePath := filepath.Join(visitsFolderName, visitsFileName)
	var count int

	data, err := os.ReadFile(visitsFilePath)
	if err != nil {
		if os.IsNotExist(err) {
			count = 1
		} else {
			return 0, err
		}
	} else {
		count, err = strconv.Atoi(strings.TrimSpace(string(data)))
		if err != nil {
			return 0, err
		}
		count++
	}

	err = os.WriteFile(visitsFilePath, []byte(strconv.Itoa(count)), 0666)
	if err != nil {
		return 0, err
	}

	return count, nil
}

// Response model with a date field
type DateResponse struct {
	Date string `json:"date"`
}

// Returns the HTML web page that displays the current date
// in the specified timezone using API
func getCurrentDateHTML(w http.ResponseWriter, r *http.Request) {
	// Log the incoming request
	log.Printf("Handling HTML page request: %s from %s", r.URL.Path, r.RemoteAddr)

	_, err := incrementVisits()
	if err != nil {
        // Even if the incrementing of visits fails, we still return the HTML page
		log.Printf("Error adding visits: %v", err)
	}

	htmlContent, err := ioutil.ReadFile(HTMLFileName)
	if err != nil {
		log.Printf("Error reading HTML file %s: %v", HTMLFileName, err)
		http.Error(w, "Internal Server Error", http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "text/html")
	w.Write(htmlContent)
}

// Returns the current date in the specified timezone
func getCurrentDate(w http.ResponseWriter, r *http.Request) {
	// Log the incoming request
	log.Printf("Handling API date request: %s from %s", r.URL.Path, r.RemoteAddr)

	_, err := incrementVisits()
	if err != nil {
	    // Even if the incrementing of visits fails, we still return the date
		log.Printf("Error adding visits: %v", err)
	}

	location, err := time.LoadLocation(timezone)
	if err != nil {
		log.Printf("Error loading timezone %s: %v", timezone, err)
		http.Error(w, "Internal Server Error", http.StatusInternalServerError)
		return
	}

	response := DateResponse{Date: time.Now().In(location).Format(dateFormat)}

	w.Header().Set("Content-Type", "application/json")
	if err := json.NewEncoder(w).Encode(response); err != nil {
		log.Printf("Error encoding JSON response: %v", err)
	}
}

// Get the number of visits to the page
func getVisits(w http.ResponseWriter, r *http.Request) {
	// Log the incoming request
	log.Printf("Handling visits request: %s from %s", r.URL.Path, r.RemoteAddr)

	visits, err := incrementVisits()
	if err != nil {
		log.Printf("Error adding visits: %v", err)
		http.Error(w, "Internal Server Error", http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "text/plain")
	w.Write([]byte("Visits: " + strconv.Itoa(visits)))
}

func main() {
	http.HandleFunc("/", getCurrentDateHTML)
	http.HandleFunc("/api/date", getCurrentDate)
	http.HandleFunc("/visits", getVisits)

	log.Printf("Starting server on port %s", appPort)
	if err := http.ListenAndServe(appPort, nil); err != nil {
		log.Fatalf("Server failed to start: %v", err)
	}
}
