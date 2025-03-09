package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
	"strconv"
	"time"

	"github.com/gin-gonic/gin"
	"github.com/prometheus/client_golang/prometheus/promhttp"
)

func main() {
	r := gin.Default()
	const VISITS_FILE = "data/visits"
	readVisits := func() int {
		if _, err := os.Stat(VISITS_FILE); os.IsNotExist(err) {
			err := ioutil.WriteFile(VISITS_FILE, []byte("0"), 0644)
			if err != nil {
				return 0
			}
		}
		data, err := ioutil.ReadFile(VISITS_FILE)
		if err != nil {
			return 0
		}
		count, _ := strconv.Atoi(string(data))
		return count
	}
	writeVisits := func(count int) {
		err := ioutil.WriteFile(VISITS_FILE, []byte(strconv.Itoa(count)), 0644)
		if err != nil {
			return
		}
	}
	r.GET("/", func(c *gin.Context) {
		moscowTime := time.Now().UTC().Add(3 * time.Hour).Format("2006-01-02 15:04:05")
		count := readVisits()
		count++
		writeVisits(count)
		c.String(http.StatusOK, fmt.Sprintf("Current time in Moscow: %s", moscowTime))
	})
	r.GET("/visits", func(c *gin.Context) {
		count := readVisits()
		c.String(http.StatusOK, fmt.Sprintf("Visits: %d", count))
	})
	r.GET("/metrics", gin.WrapH(promhttp.Handler()))
	err := r.Run(":8080")
	if err != nil {
		return
	}
}
