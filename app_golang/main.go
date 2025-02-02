package main

import (
	"fmt"
	"html/template"
	"math/rand"
	"net/http"
)

type RandomNumberData struct {
	RandomNumber int
}

func main()  {
	static_file_dir := http.Dir("static")
    file_server := http.FileServer(static_file_dir)
    http.Handle("/static/", http.StripPrefix("/static/", file_server))
	http.HandleFunc("/", handleTime)

	port := "8000" // the port on which the web application will run 
	answer := http.ListenAndServe(":"+port, nil)

	if answer != nil{
		fmt.Println("Server startup error: ", answer)
		return
	}

	fmt.Println("Server started successfully on port:", port)
}

func handleTime(w http.ResponseWriter, r *http.Request) {

	RandomNumber := rand.Intn(101) // generate a random number from 0 to 100
	data := RandomNumberData{
		RandomNumber: RandomNumber,
	}

	temp, err := template.ParseFiles("templates/index.html")
	if err != nil{
		fmt.Println("Template Error:", err)
		http.Error(w, "Wrong Tamplate", http.StatusInternalServerError)
		return
	}

	err = temp.Execute(w, data)
	if err != nil{
		fmt.Println("Error:", err)
		http.Error(w, "Error", http.StatusInternalServerError)
		return
	}
}
