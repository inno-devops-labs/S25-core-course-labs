package main

import (
	"bufio"
	"fmt"
	"html/template"
	"log"
	"log/slog"
	"net/http"
	"os"
	"path/filepath"
	"strconv"
	"sync"
	"url-shortener/internal/config"
	"url-shortener/internal/http-server/handlers/manage"
	"url-shortener/internal/http-server/handlers/url/delete"
	"url-shortener/internal/http-server/handlers/url/read"
	"url-shortener/internal/http-server/handlers/url/save"
	mwLogger "url-shortener/internal/http-server/middleware/logger"
	"url-shortener/internal/lib/logger/sl"
	"url-shortener/internal/storage/sqlite"

	"github.com/go-chi/chi/v5"
	"github.com/go-chi/chi/v5/middleware"
	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promhttp"
)

const visitsFilePath = "data/visits.txt"

var (
	httpRequestsTotal = prometheus.NewCounterVec(
		prometheus.CounterOpts{
			Name: "http_requests_total",
			Help: "Number of HTTP requests received",
		},
		[]string{"method", "path"},
	)
	visitsCount int
	visitsMutex sync.Mutex
)

func init() {
	prometheus.MustRegister(httpRequestsTotal)
	ensureDataFolder()
	loadVisits()
}

func ensureDataFolder() {
	folderPath := filepath.Dir(visitsFilePath)
	if err := os.MkdirAll(folderPath, os.ModePerm); err != nil {
		log.Fatalf("Failed to create data folder: %v", err)
	}
}

func visitMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		visitsMutex.Lock()
		visitsCount++
		saveVisits()
		visitsMutex.Unlock()
		httpRequestsTotal.WithLabelValues(r.Method, r.URL.Path).Inc()
		next.ServeHTTP(w, r)
	})
}


func loadVisits() {
	file, err := os.Open(visitsFilePath)
	if err != nil {
		if os.IsNotExist(err) {
			visitsCount = 0
			return
		}
		log.Fatalf("Failed to read visits file: %v", err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	if scanner.Scan() {
		count, err := strconv.Atoi(scanner.Text())
		if err == nil {
			visitsCount = count
		}
	}
}

func saveVisits() {
	file, err := os.Create(visitsFilePath)
	if err != nil {
		log.Printf("Failed to save visits: %v", err)
		return
	}
	defer file.Close()

	_, _ = file.WriteString(fmt.Sprintf("%d", visitsCount))
}

func main() {
	cfg := config.MustLoad()

	log := setupLogger(cfg.Env)
	log.Info("starting url-shortener", slog.String("env", cfg.Env))

	storage, err := sqlite.New(cfg.StoragePath)
	if err != nil {
		log.Error("failed to initialize storage", sl.Err(err))
		os.Exit(1)
	}

	tmpl := template.Must(template.ParseFiles("templates/manage.html"))
	router := chi.NewRouter()
	router.Use(middleware.RequestID)
	router.Use(middleware.Logger)
	router.Use(mwLogger.New(log))
	router.Use(middleware.Recoverer)
	router.Use(middleware.URLFormat)
	router.Use(func(next http.Handler) http.Handler {
		return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
			httpRequestsTotal.WithLabelValues(r.Method, r.URL.Path).Inc()
			next.ServeHTTP(w, r)
		})
	})
	router.Use(visitMiddleware)

	router.Get("/visits", func(w http.ResponseWriter, r *http.Request) {
		visitsMutex.Lock()
		count := visitsCount
		visitsMutex.Unlock()
		w.Write([]byte(fmt.Sprintf("Total visits: %d", count)))
	})

	router.Post("/urls", save.New(log, storage))
	router.Delete("/urls", delete.New(log, storage))
	router.Get("/urls/{alias}", read.New(log, storage))
	router.Get("/manage", manage.New(log, storage, tmpl))
	router.Handle("/metrics", promhttp.Handler())

	server := &http.Server{
		Addr:         cfg.Address,
		Handler:      router,
		ReadTimeout:  cfg.HttpServer.Timeout,
		WriteTimeout: cfg.HttpServer.Timeout,
		IdleTimeout:  cfg.HttpServer.IddleTimeout,
	}

	if err := server.ListenAndServe(); err != nil {
		os.Exit(1)
	}
}

func setupLogger(env string) *slog.Logger {
	var log *slog.Logger
	switch env {
	case "local":
		log = slog.New(slog.NewTextHandler(os.Stdout, &slog.HandlerOptions{Level: slog.LevelDebug}))
	case "dev":
		log = slog.New(slog.NewJSONHandler(os.Stdout, &slog.HandlerOptions{Level: slog.LevelDebug}))
	case "prod":
		log = slog.New(slog.NewJSONHandler(os.Stdout, &slog.HandlerOptions{Level: slog.LevelInfo}))
	}
	return log
}
