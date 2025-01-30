package main

import (
	"fmt"
	"net/http"
	"strconv"
	"sync"
)

var (
	mu      sync.Mutex
	counter int
)

func main() {
	http.Handle("/", http.FileServer(http.Dir("./static")))
	http.HandleFunc("/increment", incrementCounter)

	fmt.Println("Sever running on http://localhost:8080")
	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		fmt.Println("Cannot start the server:", err)
	}
}

func incrementCounter(w http.ResponseWriter, r *http.Request) {
	mu.Lock()
	counter++
	mu.Unlock()
	_, err := w.Write([]byte(strconv.Itoa(counter)))
	if err != nil {
		fmt.Println("Error writing response:", err)
	}
}
