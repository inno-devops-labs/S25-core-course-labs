package main

import (
	"fmt"
	"log"
	"net/http"
	"time"
)

func getMoscowTime(w http.ResponseWriter, r *http.Request) {
	// Load the Moscow time zone
	loc, err := time.LoadLocation("Europe/Moscow")
	if err != nil {
		http.Error(w, "Unable to load time zone", http.StatusInternalServerError)
		return
	}

	// Get the current time in Moscow
	moscowTime := time.Now().In(loc).Format("15:04:05")

	// Create the HTML content
	htmlContent := fmt.Sprintf(`
    <html>
        <body>
            <h3>Time in Moscow - %s</h3>
        </body>
    </html>
    `, moscowTime)

	// Write the HTML content to the response
	w.Header().Set("Content-Type", "text/html")
	fmt.Fprint(w, htmlContent)
}

func main() {
	http.HandleFunc("/", getMoscowTime)
	fmt.Println("Server started at localhost:8080")
	if err := http.ListenAndServe(":8080", nil); err != nil {
		log.Fatalf("Server failed to start: %v", err)
	}
}
