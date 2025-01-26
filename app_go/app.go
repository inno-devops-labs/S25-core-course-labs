package main

import (
	"fmt"
	"net/http"
)

const appPort = ":8002"

func show_time(w http.ResponseWriter, r *http.Request) {
	currentTime := get_time() // Call function from app_service.go

	w.Header().Set("Content-Type", "text/html")
	fmt.Fprintf(w, "<html><body><h1>Current Time</h1><p>%s</p></body></html>", currentTime)
}

func main() {
	fmt.Println("Server is running on http://localhost:8002/")
	http.HandleFunc("/", show_time)
	http.ListenAndServe(appPort, nil)
}
