package main

import (
	"fmt"
	"html/template"
	"math/rand"
	"net/http"
	"os"
	"strconv"
)

type RandomNumberData struct {
	RandomNumber int
	VisitCount   int 
}

var visitCount int = 0

func main() {
	loadVisits() 
	defer saveVisits() 

	staticFileDir := http.Dir("static")
	fileServer := http.FileServer(staticFileDir)
	http.Handle("/static/", http.StripPrefix("/static/", fileServer))
	http.HandleFunc("/", handleTime)
	http.HandleFunc("/visits", handleVisits)

	port := "8000" // the port on which the web application will run 
	answer := http.ListenAndServe(":"+port, nil)

	if answer != nil {
		fmt.Println("Server startup error: ", answer)
		return
	}

	fmt.Println("Server started successfully on port:", port)
}

func handleTime(w http.ResponseWriter, r *http.Request) {
	visitCount++ 
	saveVisits() 

	RandomNumber := rand.Intn(101) // generate a random number from 0 to 100
	data := RandomNumberData{
		RandomNumber: RandomNumber,
		VisitCount:   visitCount, 
	}

	temp, err := template.ParseFiles("templates/index.html")
	if err != nil {
		fmt.Println("Template Error:", err)
		http.Error(w, "Wrong Tamplate", http.StatusInternalServerError)
		return
	}

	err = temp.Execute(w, data)
	if err != nil {
		fmt.Println("Error:", err)
		http.Error(w, "Error", http.StatusInternalServerError)
		return
	}
}

func handleVisits(w http.ResponseWriter, r *http.Request) {
	temp, err := template.ParseFiles("templates/visits.html")
	if err != nil {
		fmt.Println("Template Error:", err)
		http.Error(w, "Wrong Template for visits", http.StatusInternalServerError)
		return
	}

	data := RandomNumberData{ 
		VisitCount: visitCount,
	}

	err = temp.Execute(w, data)
	if err != nil {
		fmt.Println("Error:", err)
		http.Error(w, "Error displaying visits", http.StatusInternalServerError)
		return
	}
}

func loadVisits() {
	content, err := os.ReadFile("visits.txt") 
	if err == nil {
		count, err := strconv.Atoi(string(content)) 
		if err == nil {
			visitCount = count
		} else {
			fmt.Println("Error parsing visits file:", err) 
			visitCount = 0
		}
	} else {
		fmt.Println("Error loading visits:", err) 
		visitCount = 0
	}
}

func saveVisits() {
	content := strconv.Itoa(visitCount) 
	err := os.WriteFile("visits.txt", []byte(content), 0644) 
	if err != nil {
		fmt.Println("Error saving visits:", err)
	}
}