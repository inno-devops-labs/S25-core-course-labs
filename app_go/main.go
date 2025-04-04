package main

// These are enough for working with a simple webapp
import (
	"html/template"
	"net/http"
)

var tpl = template.Must(template.ParseFiles("static/index.html"))

const PORT = "3000"

func indexHandler(w http.ResponseWriter, r *http.Request) {
	// Handler calls template to show index.html
	tpl.Execute(w, nil)
}

func main() {
	// multiplexer initialization and starting the server
	mux := http.NewServeMux()

	println("Server starting at localhost:" + PORT + "...")
	mux.HandleFunc("/", indexHandler)
	http.ListenAndServe(":"+PORT, mux)
}
