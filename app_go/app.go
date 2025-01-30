package main

import (
	"fmt"
	"log"
	"net/http"
	"os"
	"time"
)

var logger *log.Logger

func showTime(w http.ResponseWriter, r *http.Request) {
	loc, _ := time.LoadLocation("Europe/Moscow")
	currentTime := time.Now().In(loc).Format("2006-01-02 15:04:05")

	logger.Println("Served current time:", currentTime)

	fmt.Fprintf(w, `
	<html>
		<head>
			<title>Current Time in Moscow</title>
			<style>
				body { font-family: Arial, sans-serif; text-align: center; padding: 50px; }
				h1 { color: #333; }
				p { font-size: 20px; }
			</style>
		</head>
		<body>
			<h1>Current Time in Moscow</h1>
			<p>%s</p>
		</body>
	</html>`, currentTime)
}

func main() {
	logFile, err := os.OpenFile("app.log", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		log.Fatal(err)
	}
	logger = log.New(logFile, "INFO: ", log.Ldate|log.Ltime)

	logger.Println("Starting Go web application...")
	http.HandleFunc("/", showTime)
	http.ListenAndServe(":8080", nil)
}