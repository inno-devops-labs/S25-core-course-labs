package main

import (
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
	"net/url"
	"os"

	"github.com/gin-gonic/gin"
	"github.com/joho/godotenv"
)

// Types for unmarshaling json
type Response struct {
	Status map[string]interface{} `json:"status"`
	Data   Data                   `json:"data"`
}

type Data struct {
	Index Body `json:"35336"`
}

type Body struct {
	Quote Quote `json:"quote"`
}

type Quote struct {
	USD USD `json:"USD"`
}

type USD struct {
	Price float32 `json:"price"`
}

// Struct for returning currency in GET request
type currency struct {
	Coin  string  `json:"coin"`
	Price float32 `json:"price"`
}

func init() {
	if err := godotenv.Load(); err != nil {
		log.Print("No .env file")
	}
}

func main() {
	router := gin.Default()
	router.GET("/currency", getCurrency)

	router.Run("localhost:8000")
}

func trumpCurrencyRetriever() []byte {
	var API_KEY string
	API_KEY, exists := os.LookupEnv("API_KEY")
	if !exists {
		log.Print("No API key found in .env")
	}

	client := &http.Client{}
	req, err := http.NewRequest(
		"GET",
		"https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest",
		nil,
	)
	if err != nil {
		log.Print(err)
		os.Exit(1)
	}

	q := url.Values{}
	q.Add("id", "35336")

	req.Header.Set("Accepts", "application/json")
	req.Header.Add("X-CMC_PRO_API_KEY", API_KEY)
	req.URL.RawQuery = q.Encode()

	resp, err := client.Do(req)
	if err != nil {
		fmt.Println("Error sending request to server")
		os.Exit(1)
	}
	respBody, e := io.ReadAll(resp.Body)
	if e != nil {
		panic(e)
	}

	return respBody
}

func getCurrency(c *gin.Context) {
	var target Response
	error := json.Unmarshal(trumpCurrencyRetriever(), &target)
	if error != nil {
		log.Fatalf("Unable to marshal JSON due to %s", error)
	}

	currencies := []currency{
		{Coin: "ORIGINAL TRUMP", Price: target.Data.Index.Quote.USD.Price},
	}

	c.IndentedJSON(http.StatusOK, currencies)
}
