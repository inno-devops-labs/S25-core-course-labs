package main

import (
	"encoding/json"
	"fmt"
	"math/rand"
	"net/http"
	"os"
	"strconv"
	"sync"
	"time"
)

var (
	predictions = []string{
		"Today is the perfect day to start something new.",
		"Unexpected opportunities will come your way.",
		"You will achieve your goals if you stay focused.",
		"A pleasant surprise is waiting for you.",
		"Take a chance on something today—it may pay off!",
		"Trust your instincts—they won't lead you astray.",
		"A new connection will bring you happiness.",
		"Be patient—good things are on the horizon.",
		"Your hard work will soon be recognized.",
		"Spend time with loved ones—they will lift your spirits.",
	}
	counter int
	mutex   sync.Mutex
	file    = "visits/visits.txt"
)

func loadCounter() {
	data, err := os.ReadFile(file)
	if err == nil {
		if val, err := strconv.Atoi(string(data)); err == nil {
			counter = val
		}
	}
}

func saveCounter() {
	os.WriteFile(file, []byte(strconv.Itoa(counter)), 0644)
}

func predictionHandler(w http.ResponseWriter, r *http.Request) {
	mutex.Lock()
	counter++
	saveCounter()
	mutex.Unlock()

	rand.Seed(time.Now().UnixNano())
	randomPrediction := predictions[rand.Intn(len(predictions))]
	fmt.Println(randomPrediction)

	response := map[string]string{"prediction": randomPrediction}
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(response)
}

func visitsHandler(w http.ResponseWriter, r *http.Request) {
	mutex.Lock()
	defer mutex.Unlock()
	response := map[string]int{"visits": counter}
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(response)
}

func main() {
	loadCounter()
	http.HandleFunc("/", predictionHandler)
	http.HandleFunc("/visits", visitsHandler)

	http.ListenAndServe(":8080", nil)
}
