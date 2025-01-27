package main

import (
	"fmt"
	"html/template"
	"math/rand"
	"net/http"
)

type Random_Number_Data struct {
	Random_Number int
}

func main()  {
	static_file_dir := http.Dir("static")
    file_server := http.FileServer(static_file_dir)
    http.Handle("/static/", http.StripPrefix("/static/", file_server))
	http.HandleFunc("/", handle_time)

	port := "8000" // the port on which the web application will run 
	answer := http.ListenAndServe(":"+port, nil)

	if answer != nil{
		fmt.Println("Server startup error: ", answer)
		return
	} else {
		fmt.Println("Server started successfully on port:", port)
	} 
}

func handle_time(w http.ResponseWriter, r *http.Request) {

	random_number := rand.Intn(101) // generate a random number from 0 to 100
	data := Random_Number_Data{
		Random_Number: random_number,
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
