package main

import (
	"fmt"
	"net/http"
	"regexp"
	"strings"
	"sync"
	"time"
)

var (
	linuxReleaseDate = time.Date(1991, time.October, 5, 0, 0, 0, 0, time.UTC)
	sharedValue      = "None"
	mutex            sync.RWMutex
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

		// Extract the 'Link' section from header
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
				fmt.Println("Number of commits in the Linux kernel:", numberOfCommits)
			} else {
				fmt.Println("Data about commits is not found...")
			}
		}

		err = resp.Body.Close()
		if err != nil {
			println("Couldnt close response body: ", err.Error())
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

	years, months, days := timePassedSince(linuxReleaseDate)

	html := `
	<!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>Linux Kernel Data</title>
		<style>
			body { font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f4f4f9; color: #333; }
			header { background-color: #333; color: #fff; padding: 10px 20px; text-align: center; }
			main { padding: 20px; text-align: center; }
			.container { max-width: 600px; margin: 0 auto; }
			.info { background: #fff; padding: 15px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); }
		</style>
	</head>
	<body>
		<header>
			<h1>Linux Kernel Repository Statistics</h1>
		</header>
		<main>
			<div class="container">
				<div class="info">
					<p><strong>Number of commits:</strong> ` + numberOfCommits + `</p>
					<p><strong>Time passed since Linux 0.02 release:</strong></p>
					<p>` + fmt.Sprintf("%d years, %d months, %d days", years, months, days) + `</p>
				</div>
			</div>
		</main>
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

func main() {
	// Start the background updater
	go updateKernelRepositoryData()

	// Set up HTTP server
	http.HandleFunc("/", handler)

	fmt.Println("Server running on http://localhost:8080")
	err := http.ListenAndServe(":8080", nil)

	if err != nil {
		println("Server died with error: ", err.Error())
	}
}
