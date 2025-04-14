package main

import (
	"encoding/json"
	"fmt"
	"math/rand"
	"net/http"
	"time"
)

func main() {
	predictions := []string{
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

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		rand.Seed(time.Now().UnixNano())
		randomPrediction := predictions[rand.Intn(len(predictions))]

        fmt.Println(randomPrediction)

		response := map[string]string{"prediction": randomPrediction}
		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(response)
	})

	http.ListenAndServe(":8080", nil)
}
