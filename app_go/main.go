package main

import (
	"fmt"
	"net/http"
	"time"
)

func moscowTimeHandler(w http.ResponseWriter, r *http.Request) {
	// Load Moscow's timezone location
	location, err := time.LoadLocation("Europe/Moscow")
	if err != nil {
		http.Error(w, "Error loading timezone", http.StatusInternalServerError)
		return
	}

	// Get current time in Moscow
	moscowTime := time.Now().In(location)

	// Format and display the time
	fmt.Fprintf(w, "Current time in Moscow: %s", moscowTime.Format("2006-01-02 15:04:05 MST"))
}

func main() {
	http.HandleFunc("/", moscowTimeHandler)
	fmt.Println("Server started on :8080")
	http.ListenAndServe(":8080", nil)
}
