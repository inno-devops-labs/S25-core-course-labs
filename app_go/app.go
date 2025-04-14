package main

import (
	"html/template"
	"log"
	"net/http"
	"time"

	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promhttp"
)

// Define a counter metric
var requestCount = prometheus.NewCounter(
	prometheus.CounterOpts{
		Name: "app_requests_total",
		Help: "Total number of requests",
	},
)

func init() {
	// Register the counter with Prometheus
	prometheus.MustRegister(requestCount)
}

// PageData holds the data that will be passed to the HTML template.
type PageData struct {
	CurrentTime string // Formatted current time in Moscow
}

// templates is a global variable to store parsed templates to avoid reloading them on every request.
var templates *template.Template

// showCurrentTimeMoscow fetches the current time in Moscow and returns it as a formatted string.
func showCurrentTimeMoscow() string {
	// Load the Moscow time zone
	location, err := time.LoadLocation("Europe/Moscow")
	if err != nil {
		log.Println("Error loading location:", err)
		return "Error fetching time" // Return an error message if the location fails to load
	}

	// Get the current time in Moscow
	currentTime := time.Now().In(location)
	return currentTime.Format("15:04:05") // Format as HH:MM:SS
}

// Home handles requests to the root URL ("/") and renders the HTML template with the current time.
func Home(w http.ResponseWriter, r *http.Request) {

	// Increment the request counter
	requestCount.Inc()

	if templates == nil {
		var err error
		templates, err = template.ParseFiles("templates/index.html")
		if err != nil {
			http.Error(w, "Error loading template", http.StatusInternalServerError)
			log.Println("Template loading error:", err)
			return
		}
	}

	data := PageData{
		CurrentTime: showCurrentTimeMoscow(),
	}

	err := templates.ExecuteTemplate(w, "index.html", data)
	if err != nil {
		http.Error(w, "Error rendering template", http.StatusInternalServerError)
		log.Println("Template execution error:", err)
	}
}

func main() {
	// Parse templates once at startup to improve efficiency
	templates = template.Must(template.ParseFiles("templates/index.html"))

	// Register the home handler for the root path
	http.HandleFunc("/", Home)

	// Expose Prometheus metrics on /metrics
	http.Handle("/metrics", promhttp.Handler())

	// Start the HTTP server on port 3000
	log.Println("Starting server on :3500...")
	err := http.ListenAndServe("0.0.0.0:3500", nil)
	if err != nil {
		log.Fatal("Server failed:", err) // Log and exit if the server fails to start
	}
}