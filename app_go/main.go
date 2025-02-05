package main

import (
	"fmt"
	"net/http"
	"time"
)

func handler(w http.ResponseWriter, r *http.Request) {
	location, _ := time.LoadLocation("Europe/Moscow")
	currentTime := time.Now().In(location)
	fmt.Fprintf(w, `{"moscow_time": "%s"}`, currentTime.Format(time.RFC3339))
}

func main() {
	http.HandleFunc("/", handler)
	http.ListenAndServe(":8080", nil)
}
