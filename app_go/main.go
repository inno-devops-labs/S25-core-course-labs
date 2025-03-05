package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"html/template"
	"log"
	"net/http"
	"time"
)

func main() {
	r := gin.Default()

	r.GET("/", func(c *gin.Context) {
		log.Println("Request received at root endpoint")

		// Get the current date in Moscow timezone
		loc, err := time.LoadLocation("Europe/Moscow")
		if err != nil {
			log.Printf("Error loading timezone: %v", err)
			c.String(http.StatusInternalServerError, "Internal Server Error")
			return
		}
		currentDate := time.Now().In(loc)
		y, m, d := currentDate.Date()
		formattedDate := fmt.Sprintf("%d %s %d", y, m, d)

		// Generate the HTML response
		tmpl := `
    <html>
      <head>
        <title>Moscow Date</title>
      </head>
      <body>
        <p>Date in Moscow</p>
        <p> {{.}} </p>
      </body>
    </html>`

		parsedTmpl, err := template.New("webpage").Parse(tmpl)
		if err != nil {
			log.Printf("Error parsing template: %v", err)
			c.String(http.StatusInternalServerError, "Internal Server Error")
			return
		}

		c.Header("Content-Type", "text/html; charset=utf-8")
		if err := parsedTmpl.Execute(c.Writer, formattedDate); err != nil {
			log.Printf("Error executing template: %v", err)
			c.String(http.StatusInternalServerError, "Internal Server Error")
			return
		}
	})

	r.Run(":8080")
}
