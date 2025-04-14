package main

import (
	"encoding/json"
	"net/http"
)

type GreetingResponse struct {
	Greeting string `json:"greeting"`
}

func greetHandler(w http.ResponseWriter, r *http.Request) {
	// Parse the name from query parameters
	name := r.URL.Query().Get("name")
	if name == "" {
		name = "Guest" // Default to "Guest" if no name is provided
	}

	// Create the response structure
	response := GreetingResponse{
		Greeting: "Hello, " + name + "! Welcome!",
	}

	// Set content type and respond with JSON
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)
	json.NewEncoder(w).Encode(response)
}

func main() {
	http.HandleFunc("/greet", greetHandler)
	println("Server is running on http://localhost:8000")
	http.ListenAndServe(":8000", nil)
}
