package handlers

import (
	"html/template"
	"net/http"
	"path/filepath"

	"app_golang/utils"
)

// Handler function to display the current time in Moscow
func CurrentTimeHandler(w http.ResponseWriter, r *http.Request) {
	currentTime := utils.GetCurrentTimeInMoscow()

	// Get the absolute path for templates directory
	tmplPath := filepath.Join("templates", "index.html")
	tmpl, err := template.ParseFiles(tmplPath)
	if err != nil {
		http.Error(w, "Could not load template", http.StatusInternalServerError)
		return
	}

	tmpl.Execute(w, currentTime)
}
