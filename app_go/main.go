package main

import (
	"encoding/json"
	"log"
	"net/http"
	"time"
)

type Response struct {
	DayOfWeek string `json:"day_of_week"`
}

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		loc, err := time.LoadLocation("Europe/Moscow")
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}

		moscowTime := time.Now().In(loc)
		dayOfWeek := moscowTime.Weekday().String()

		response := Response{
			DayOfWeek: dayOfWeek,
		}

		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(response)
	})

	log.Printf("Server starting on http://localhost:8080")
	if err := http.ListenAndServe(":8080", nil); err != nil {
		log.Fatal(err)
	}
} 