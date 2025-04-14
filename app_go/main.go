package main

import (
    "fmt"
    "log"
    "net/http"
    "time"
)

func moscowTimeHandler(w http.ResponseWriter, r *http.Request) {
    // Set Moscow timezone
    loc, err := time.LoadLocation("Europe/Moscow")
    if err != nil {
        http.Error(w, "Could not load Moscow timezone", http.StatusInternalServerError)
        return
    }
    
    currentTime := time.Now().In(loc).Format("2006-01-02 15:04:05")
    fmt.Fprintf(w, "<h1>Current Time in Moscow: %s</h1>", currentTime)
}

func main() {
    http.HandleFunc("/", moscowTimeHandler)
    fmt.Println("Server started at http://localhost:8080")
    log.Fatal(http.ListenAndServe(":8080", nil))
}

