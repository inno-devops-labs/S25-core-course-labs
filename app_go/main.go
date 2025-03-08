package main

import (
	"fmt"
	"net/http"
	"regexp"
	"strconv"
	"strings"
	"sync"
	"time"
	"os"

	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promhttp"
)

var (
	linuxReleaseDate = time.Date(1991, time.October, 5, 0, 0, 0, 0, time.UTC)
	sharedValue      = "None"
	mutex            sync.RWMutex
	visitsFile  = "/data/visits.txt"

	// Prometheus metric: Tracks number of commits
	commitCounter = prometheus.NewGauge(prometheus.GaugeOpts{
		Name: "linux_kernel_commits",
		Help: "Number of commits in the Linux kernel repository",
	})
)

// Queries the GitHub API for the number of commits
func updateKernelRepositoryData() {
	url := "https://api.github.com/repos/torvalds/linux/commits?sha=master&per_page=1&page=1"
	re := regexp.MustCompile(`page=(\d+)>;`)

	for {
		resp, err := http.Get(url)
		if err != nil {
			fmt.Println("Error fetching data:", err)
			time.Sleep(20 * time.Minute)
			continue
		}

		linkHeader := resp.Header.Get("link")
		if linkHeader == "" {
			fmt.Println("Link header is not present in the response")
		} else {
			data := strings.Split(linkHeader, " ")
			matches := re.FindStringSubmatch(data[2])

			if len(matches) > 1 {
				numberOfCommits := matches[1]

				mutex.Lock()
				sharedValue = numberOfCommits
				mutex.Unlock()

				// Convert string to float64 for Prometheus
				commitCount, err := strconv.ParseFloat(numberOfCommits, 64)
				if err != nil {
					fmt.Println("Error converting commit count:", err)
				} else {
					commitCounter.Set(commitCount) // Update Prometheus metric
				}

				fmt.Println("Number of commits in the Linux kernel:", numberOfCommits)
			} else {
				fmt.Println("Data about commits is not found...")
			}
		}

		err = resp.Body.Close() // Close response body

		if err != nil {
			fmt.Println("Something went wrong closing body...")
		}

		time.Sleep(10 * time.Second)
	}
}

// Calculates the time passed since a given date in years, months, and days
func timePassedSince(date time.Time) (years, months, days int) {
	currentTime := time.Now()

	years = currentTime.Year() - date.Year()
	months = int(currentTime.Month()) - int(date.Month())
	if months < 0 {
		years--
		months += 12
	}

	days = currentTime.Day() - date.Day()
	if days < 0 {
		previousMonth := currentTime.AddDate(0, -1, 0)
		days += time.Date(previousMonth.Year(), previousMonth.Month(), 1, 0, 0, 0, 0, time.UTC).AddDate(0, 1, -1).Day()
		months--
		if months < 0 {
			years--
			months += 12
		}
	}

	return
}

// HTTP handler to serve the homepage
func handler(w http.ResponseWriter, r *http.Request) {
	mutex.RLock()
	numberOfCommits := sharedValue
	mutex.RUnlock()
	incrementVisitCount()

	years, months, days := timePassedSince(linuxReleaseDate)

	html := `
	<!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset="UTF-8">
		<title>Linux Kernel Data</title>
	</head>
	<body>
		<h1>Linux Kernel Repository Statistics</h1>
		<p><strong>Number of commits:</strong> ` + numberOfCommits + `</p>
		<p><strong>Time passed since Linux 0.02 release:</strong> ` + fmt.Sprintf("%d years, %d months, %d days", years, months, days) + `</p>
	</body>
	</html>
	`
	w.Header().Set("Content-Type", "text/html")
	w.WriteHeader(http.StatusOK)
	_, err := w.Write([]byte(html))
	if err != nil {
		println("Couldn't write header: ", err.Error())
	}
}

// Registers Prometheus metrics
func initMetrics() {
	prometheus.MustRegister(commitCounter)
}

func getVisitCount() int {
	if _, err := os.Stat(visitsFile); os.IsNotExist(err) {
		return 0
	}

	data, err := os.ReadFile(visitsFile)
	if err != nil {
		fmt.Println("Error reading visit count:", err)
		return 0
	}

	count, err := strconv.Atoi(strings.TrimSpace(string(data)))
	if err != nil {
		fmt.Println("Error parsing visit count:", err)
		return 0
	}


	return count
}

func incrementVisitCount() int {
	count := getVisitCount() + 1
	if err := os.WriteFile(visitsFile, []byte(strconv.Itoa(count)), 0644); err != nil {
		fmt.Println("Error writing visit count:", err)
	}
	return count
}

func visitHandler(w http.ResponseWriter, r *http.Request) {
	count := incrementVisitCount()

	html := fmt.Sprintf(`
	<!DOCTYPE html>
	<html>
	<head>
		<title>Visit Counter</title>
	</head>
	<body>
		<h1>Number of Visits</h1>
		<p><strong>Visits:</strong> %d</p>
	</body>
	</html>
	`, count)

	w.Header().Set("Content-Type", "text/html")
	w.WriteHeader(http.StatusOK)
	_, err := w.Write([]byte(html))
	if err != nil {
		fmt.Println("Error writing response:", err)
	}
}


func main() {
	// Register Prometheus metrics
	initMetrics()

	// Start background updater
	go updateKernelRepositoryData()

	// HTTP handlers
	http.HandleFunc("/", handler)
	http.Handle("/metrics", promhttp.Handler()) // Prometheus endpoint

	http.HandleFunc("/visit", visitHandler)

	fmt.Println("Server running on http://localhost:8080")
	fmt.Println("Metrics available on http://localhost:8080/metrics")

	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		println("Server died with error: ", err.Error())
	}
}
