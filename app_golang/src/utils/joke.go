package utils

import (
	"encoding/json"
	"io"
	"net/http"

	"github.com/gin-gonic/gin"
)

// The joke struct
type Joke struct {
	Error    bool   `json:"error"`
	Category string `json:"category"`
	Type     string `json:"type"`
	Joke     string `json:"joke,omitempty"`
	Setup    string `json:"setup,omitempty"`
	Delivery string `json:"delivery,omitempty"`
	Flags    struct {
		Nsfw      bool `json:"nsfw"`
		Religious bool `json:"religious"`
		Political bool `json:"political"`
		Racist    bool `json:"racist"`
		Sexist    bool `json:"sexist"`
		Explicit  bool `json:"explicit"`
	} `json:"flags"`
	Id   int    `json:"id"`
	Safe bool   `json:"safe"`
	Lang string `json:"lang"`
}

// Returns a random joke from the public API.
func JokeFromAPI(c *gin.Context) Joke {
	var joke Joke

	// Create a GET request to the Joke API
	req, err := http.NewRequest("GET", "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit", nil)
	if err != nil {
		c.JSON(http.StatusFailedDependency, gin.H{
			"error": err.Error(),
		})
		panic(err)
	}

	// Do the request
	client := &http.Client{}
	resp, err := client.Do(req)

	// If request was not successful, return error
	if err != nil {
		c.JSON(http.StatusFailedDependency, gin.H{
			"error": err.Error(),
		})
		panic(err)
	}

	// Read the body response
	defer resp.Body.Close()
	body, err := io.ReadAll(resp.Body)

	// If body was not read successfully, return error
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{
			"error": err.Error(),
		})
		panic(err)
	}

	// Unmarshal json to struct
	err = json.Unmarshal(body, &joke)

	// If unmarshal was not successful, return error
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{
			"error": err.Error(),
		})
		panic(err)
	}

	// Return joke
	return joke
}
