package main

import (
	"fmt"
	"html/template"
	"net/http"

	"app_golang/utils"
)

// Handler function to display the current time in Moscow
func currentTimeHandler(w http.ResponseWriter, r *http.Request) {
	currentTime := utils.GetCurrentTimeInMoscow()
	tmpl, err := template.ParseFiles("templates/index.html")
	if err != nil {
		http.Error(w, "Could not load template", http.StatusInternalServerError)
		return
	}
	tmpl.Execute(w, currentTime)
}

func main() {
	http.HandleFunc("/", currentTimeHandler)
	fmt.Println("Starting server at :8080")
	if err := http.ListenAndServe(":8080", nil); err != nil {
		fmt.Println("Error starting server:", err)
	}
}
