package main

import (
	"html/template"
	"log"
	"math/rand"
	"net/http"
	"os"
	"strings"
	"time"
)

// Global variable to store quotes
var quotes []string

// LoadQuotes reads quotes from a file and populates the quotes slice
func LoadQuotes(filename string) {
	file, err := os.ReadFile(filename)
	if err != nil {
		log.Fatalf("Failed to read quotes file: %v", err)
	}
	// Split file contents into lines
	quotes = strings.Split(strings.TrimSpace(string(file)), "\n")
}

// randomQuoteHandler renders the HTML template with a random quote
func randomQuoteHandler(w http.ResponseWriter, r *http.Request) {
	// Seed random number generator
	rand.Seed(time.Now().UnixNano())

	// Select a random quote
	randomIndex := rand.Intn(len(quotes))
	randomQuote := quotes[randomIndex]

	// Parse the HTML template
	tmpl, err := template.ParseFiles("templates/index.html")
	if err != nil {
		http.Error(w, "Failed to load template", http.StatusInternalServerError)
		log.Printf("Template error: %v", err)
		return
	}

	// Render the template with the random quote
	err = tmpl.Execute(w, map[string]string{"Quote": randomQuote})
	if err != nil {
		http.Error(w, "Failed to render template", http.StatusInternalServerError)
		log.Printf("Template execution error: %v", err)
	}
}

func main() {
	LoadQuotes("quotes.txt")

	// Set up the route and start the server
	http.HandleFunc("/", randomQuoteHandler)
	log.Println("Starting server at http://localhost:8080")
	log.Fatal(http.ListenAndServe(":8080", nil))
}
