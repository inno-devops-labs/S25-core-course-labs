package main

import (
	"encoding/json"
	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promhttp"
	"html/template"
	"io"
	"log"
	"net/http"
	"strconv"
	"strings"
	"sync"
	"time"
)

type PageData struct {
	Forks string
}

type statusRecordingResponseWriter struct {
	http.ResponseWriter
	statusCode int
}

func (rw *statusRecordingResponseWriter) WriteHeader(code int) {
	rw.statusCode = code
	rw.ResponseWriter.WriteHeader(code)
}

var requestCount = prometheus.NewCounterVec(
	prometheus.CounterOpts{
		Name: "request_count",
		Help: "Total number of requests processed by the Go application",
	},
	[]string{"app_name", "method", "endpoint", "http_status"})

var requestLatency = prometheus.NewHistogramVec(
	prometheus.HistogramOpts{
		Name:    "request_latency_seconds",
		Help:    "Request latency in seconds",
		Buckets: prometheus.DefBuckets, // or define your own buckets
	},
	[]string{"app_name", "endpoint"},
)

func loggingMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		startTime := time.Now()

		log.Printf("[%s] %s %s from %s", startTime.Format(time.RFC3339), r.Method, r.URL.Path, r.RemoteAddr)

		next.ServeHTTP(w, r)
	})
}

func metricsMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		startTime := time.Now()

		rr := &statusRecordingResponseWriter{ResponseWriter: w, statusCode: http.StatusOK}
		next.ServeHTTP(rr, r)

		elapsed := time.Since(startTime).Seconds()

		requestLatency.WithLabelValues("app_go", r.URL.Path).Observe(elapsed)
		requestCount.WithLabelValues(
			"my_go_app",
			r.Method,
			r.URL.Path,
			strconv.Itoa(rr.statusCode),
		).Inc()
	})
}

func main() {
	amountMutex := sync.Mutex{}
	amountCalculated := false
	var amount int

	initialRepo := "https://api.github.com/repos/inno-devops-labs/S25-core-course-labs/forks?per_page=100"

	ticker := time.NewTicker(5 * time.Second)
	quit := make(chan struct{})
	go func() {
		for {
			select {
			case <-ticker.C:
				repo := initialRepo
				currAmount := 0
			loop:
				for {
					get, err := http.Get(repo)
					if err != nil {
						log.Printf("Error fetching repos: %v", err)
						continue
					}
					body, err := io.ReadAll(get.Body)
					if err != nil {
						log.Printf("Error reading body: %v", err)
						continue
					}
					var val []map[string]interface{}
					err = json.Unmarshal(body, &val)
					if err != nil {
						log.Printf("Error unmarshalling body: %v", err)
						continue
					}
					currAmount += len(val)
					pages := strings.Split(get.Header.Get("link"), ", ")
					for _, page := range pages {
						currPage := strings.Split(page, "; ")
						if len(currPage) == 2 {
							if strings.Contains(currPage[1], "next") {
								repo = strings.Trim(currPage[0], "<>")
								continue loop
							}
						}
					}
					amountMutex.Lock()
					amount = currAmount
					amountCalculated = true
					amountMutex.Unlock()
					break loop
				}
			case <-quit:
				ticker.Stop()
				return
			}
		}
	}()

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		amountMutex.Lock()
		data := PageData{}
		data.Forks = "Loading. Please wait..."
		if amountCalculated {
			data.Forks = strconv.Itoa(amount)
		}
		amountMutex.Unlock()
		// Parse and execute the template
		tmpl, err := template.ParseFiles("./templates/index.html")
		if err != nil {
			log.Printf("Error parsing template: %v", err)
			http.Error(w, "Failed to parse template", http.StatusInternalServerError)
			return
		}

		err = tmpl.Execute(w, data)
		if err != nil {
			log.Printf("Error executing template: %v", err)
			http.Error(w, "Failed to execute template", http.StatusInternalServerError)
			return
		}
	})

	http.HandleFunc("/health", func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusOK)
		w.Write([]byte("OK"))
	})

	http.Handle("/metrics", promhttp.Handler())

	err := http.ListenAndServe(":8080", loggingMiddleware(http.DefaultServeMux))
	if err != nil {
		log.Fatal(err)
		return
	}
	defer close(quit)
}
