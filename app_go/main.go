package main

import (
	"time"
	"net/http"
	"io/ioutil"
	"encoding/json"
)

type DateResponse struct {
	Date string `json:"date"`
}

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		htmlContent, err := ioutil.ReadFile("index.html")

		if err != nil {
			http.Error(w, "Internal Server Error", http.StatusInternalServerError)
			return
		}

		w.Header().Set("Content-Type", "text/html")
		w.Write(htmlContent)
	})

	http.HandleFunc("/api/date", func(w http.ResponseWriter, r *http.Request) {
		location, err := time.LoadLocation("Europe/Moscow")

		if err != nil {
			http.Error(w, "Internal Server Error", http.StatusInternalServerError)
			return
		}

		response := DateResponse{Date: time.Now().In(location).Format("2006-01-02"),}

		w.Header().Set("Content-Type", "application/json")
	    json.NewEncoder(w).Encode(response)
	})

	http.ListenAndServe(":8002", nil)
}
