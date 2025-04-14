package main

import (
	"fmt"
	"net/http"
	"time"

	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promhttp"
)

// Define custom metrics
var (
	requestCounter = prometheus.NewCounter(prometheus.CounterOpts{
		Name: "moscow_time_requests_total",
		Help: "Total number of requests to the Moscow time endpoint.",
	})

	requestLatency = prometheus.NewHistogram(prometheus.HistogramOpts{
		Name:    "moscow_time_request_latency_seconds",
		Help:    "Request latency in seconds for the Moscow time endpoint.",
		Buckets: prometheus.ExponentialBuckets(0.001, 2, 10), // Buckets for latency measurement
	})
)

func init() {
	// Register custom metrics with Prometheus
	prometheus.MustRegister(requestCounter)
	prometheus.MustRegister(requestLatency)
}

func moscowTimeHandler(w http.ResponseWriter, r *http.Request) {
	// Start timing the request
	start := time.Now()

	// Load Moscow's timezone location
	location, err := time.LoadLocation("Europe/Moscow")
	if err != nil {
		http.Error(w, "Error loading timezone", http.StatusInternalServerError)
		return
	}

	// Get current time in Moscow
	moscowTime := time.Now().In(location)

	// Format and display the time
	fmt.Fprintf(w, "Current time in Moscow: %s\n", moscowTime.Format("2006-01-02 15:04:05 MST"))

	// Record the request as completed
	requestCounter.Inc()

	// Calculate and record the latency
	duration := time.Since(start).Seconds()
	requestLatency.Observe(duration)
}

func main() {
	// Set up the handler for the main endpoint
	http.HandleFunc("/", moscowTimeHandler)

	// Expose metrics at /metrics
	http.Handle("/metrics", promhttp.Handler())

	// Start the server
	fmt.Println("Server started on :8080")
	if err := http.ListenAndServe(":8080", nil); err != nil {
		fmt.Printf("Error starting server: %v\n", err)
	}
}
