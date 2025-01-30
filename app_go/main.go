package main

import (
	"fmt"
	"net/http"
	"time"
)

func innoTimeHandler(w http.ResponseWriter, r *http.Request) {
	loc, err := time.LoadLocation("Europe/Moscow")
	if err != nil {
		http.Error(w, "Error loading time zone", http.StatusInternalServerError)
		return
	}
	currentTime := time.Now().In(loc).Format("2006-01-02 15:04:05")
	fmt.Fprintf(w, "<h1>Current time in Innopolis: %s</h1>", currentTime)
}

func main() {
	http.HandleFunc("/", innoTimeHandler)
	port := ":8080"
	http.ListenAndServe(port, nil)
}
