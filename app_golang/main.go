package main

import (
	"fmt"
	"net/http"
	"time"

	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promhttp"
)

var (
	requestsTotal = prometheus.NewCounter(
		prometheus.CounterOpts{
			Name: "http_requests_total",
			Help: "Total number of HTTP requests",
		},
	)
	requestDuration = prometheus.NewHistogram(
		prometheus.HistogramOpts{
			Name:    "http_request_duration_seconds",
			Help:    "Histogram of response time for /msc_time",
			Buckets: prometheus.DefBuckets,
		},
	)
)

func init() {
	prometheus.MustRegister(requestsTotal)
	prometheus.MustRegister(requestDuration)
}

func GetMoscowTime(w http.ResponseWriter, r *http.Request) {
	start := time.Now()
	requestsTotal.Inc()

	loc, err := time.LoadLocation("Europe/Moscow")
	if err != nil {
		http.Error(w, "Unable to load Moscow timezone", http.StatusInternalServerError)
		return
	}
	moTime := time.Now().In(loc)
	fmt.Fprintf(w, `{"current_time_in_moscow": "%s"}`, moTime)

	duration := time.Since(start).Seconds()
	requestDuration.Observe(duration)
}

func main() {
	http.HandleFunc("/msc_time", GetMoscowTime)
	http.Handle("/metrics", promhttp.Handler())

	fmt.Println("Starting server on :8080...")
	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		panic("error starting http server")
	}
}
