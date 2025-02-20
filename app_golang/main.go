package main

import (
	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promhttp"
	"html/template"
	"log"
	"math/rand"
	"net/http"
	"os"
	"strconv"
	"strings"
	"time"
)

// Global variable to store quotes
var quotes []string

// Prometheus metrics
var (
	requestCount = prometheus.NewCounterVec(
		prometheus.CounterOpts{
			Name: "request_count",
			Help: "Total number of requests processed by the Go application",
		},
		[]string{"app_name", "method", "endpoint", "http_status"},
	)

	requestLatency = prometheus.NewHistogramVec(
		prometheus.HistogramOpts{
			Name:    "request_latency_seconds",
			Help:    "Request latency in seconds",
			Buckets: prometheus.DefBuckets, // or define your own buckets
		},
		[]string{"app_name", "endpoint"},
	)
)

// LoadQuotes reads quotes from a file and populates the quotes slice
func LoadQuotes(filename string) {
	file, err := os.ReadFile(filename)
	if err != nil {
		log.Fatalf("Failed to read quotes file: %v", err)
	}
	// Split file contents into lines
	quotes = strings.Split(strings.TrimSpace(string(file)), "\n")
}

// randomQuoteHandler renders the HTML template with a random quote
func randomQuoteHandler(w http.ResponseWriter, r *http.Request) {
	// Seed random number generator
	src := rand.NewSource(time.Now().UnixNano())
	rng := rand.New(src)

	// Select a random quote
	randomIndex := rng.Intn(len(quotes))
	randomQuote := quotes[randomIndex]

	// Parse the HTML template
	tmpl, err := template.ParseFiles("templates/index.html")
	if err != nil {
		http.Error(w, "Failed to load template", http.StatusInternalServerError)
		log.Printf("Template error: %v", err)
		return
	}

	// Render the template with the random quote
	err = tmpl.Execute(w, map[string]string{"Quote": randomQuote})
	if err != nil {
		http.Error(w, "Failed to render template", http.StatusInternalServerError)
		log.Printf("Template execution error: %v", err)
	}
}

func loggingMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		startTime := time.Now()

		// Log request details
		log.Printf("[%s] %s %s from %s",
			startTime.Format(time.RFC3339),
			r.Method,
			r.URL.Path,
			r.RemoteAddr,
		)

		next.ServeHTTP(w, r)
	})
}

// statusRecordingResponseWriter helps capture the HTTP status code
type statusRecordingResponseWriter struct {
	http.ResponseWriter
	statusCode int
}

func (rw *statusRecordingResponseWriter) WriteHeader(code int) {
	rw.statusCode = code
	rw.ResponseWriter.WriteHeader(code)
}

// metricsMiddleware updates Prometheus metrics for each request
func metricsMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		startTime := time.Now()

		// We wrap the original ResponseWriter to capture status code
		rr := &statusRecordingResponseWriter{ResponseWriter: w, statusCode: http.StatusOK}
		next.ServeHTTP(rr, r)

		// Calculate request latency
		elapsed := time.Since(startTime).Seconds()

		// Update Prometheus metrics
		requestLatency.WithLabelValues("my_go_app", r.URL.Path).Observe(elapsed)
		requestCount.WithLabelValues(
			"my_go_app",
			r.Method,
			r.URL.Path,
			strconv.Itoa(rr.statusCode),
		).Inc()
	})
}

func healthHandler(w http.ResponseWriter, r *http.Request) {
    w.WriteHeader(http.StatusOK)
    w.Write([]byte("OK"))
}

func main() {
	LoadQuotes("quotes.txt")

	// Register Prometheus metrics
	prometheus.MustRegister(requestCount, requestLatency)

	mux := http.NewServeMux()
	mux.HandleFunc("/", randomQuoteHandler)
	mux.HandleFunc("/health", healthHandler)

	mux.Handle("/metrics", promhttp.Handler())

	// Set up the route and start the server
	wrappedMux := loggingMiddleware(metricsMiddleware(mux))
	log.Println("Starting server at http://localhost:8080")
	log.Fatal(http.ListenAndServe(":8080", wrappedMux))
}
