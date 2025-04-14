package main

import (
	"fmt"
	"net/http"
	"time"
)

func GetMoscowTime(w http.ResponseWriter, r *http.Request) {
	loc, err := time.LoadLocation("Europe/Moscow")
	if err != nil {
		http.Error(w, "Unable to load Moscow timezone", http.StatusInternalServerError)
		return
	}
	moTime := time.Now().In(loc)
	fmt.Fprintf(w, `{"current_time_in_moscow": "%s"}`, moTime)
}

func main() {
	http.HandleFunc("/msc_time", GetMoscowTime)

	// Start the server on port 8080
	fmt.Println("Starting server on :8080...")
	http.ListenAndServe(":8080", nil)
}
