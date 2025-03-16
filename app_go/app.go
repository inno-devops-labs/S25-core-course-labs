package main

import (
	"fmt"
	"net/http"
	"io/ioutil"
	"log"
	"os"
	"strconv"
	"strings"
)

const appPort = ":8002"
const visitsFile = "./data/visits"

// Ensure data directory exists
func init() {
	os.MkdirAll("data", os.ModePerm)
}
func getVisits() int {
	data, err := ioutil.ReadFile(visitsFile)
	if err != nil {
		return 0
	}
	count, err := strconv.Atoi(strings.TrimSpace(string(data)))
	if err != nil {
		return 0
	}
	return count
}

func incrementVisits() int {
	count := getVisits() + 1
	// Ensure the data directory exists
	if err := os.MkdirAll("./data", 0755); err != nil {
		log.Printf("Error creating data directory: %v", err)
	}
	if err := ioutil.WriteFile(visitsFile, []byte(strconv.Itoa(count)), 0644); err != nil {
		log.Printf("Error writing visits file: %v", err)
	}
	return count
}

func show_time(w http.ResponseWriter, r *http.Request) {
	currentTime := get_time() // Call function from app_service.go
	incrementVisits()

	w.Header().Set("Content-Type", "text/html")
	fmt.Fprintf(w, "<html><body><h1>Current Time</h1><p>%s</p></body></html>", currentTime)
}

func showVisits(w http.ResponseWriter, r *http.Request) {
    log.Println("Visits endpoint hit!") // Debugging log
    count := getVisits()
    w.Header().Set("Content-Type", "text/plain")
    fmt.Fprintf(w, "Total visits: %d", count)
}


func main() {
	fmt.Println("Server is running on http://localhost:8002/")
	
	http.HandleFunc("/", show_time)
	http.HandleFunc("/visits", showVisits)
	http.ListenAndServe(appPort, nil)
}
