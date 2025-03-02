package utils

import (
	"fmt"
	"log"
	"os"
)

var Counter int = 0

func IncrementCounter() {
	Counter += 1
	os.MkdirAll("visits", 0666)
	file, err := os.Create("./visits/visits")

	if err != nil {
		log.Fatal(err)
	}

	_, err = file.Seek(0, 0)

	if err != nil {
		log.Fatal(err)
	}

	_, err = fmt.Fprintf(file, "%d", Counter)

	if err != nil {
		log.Fatal(err)
	}

	file.Close()
}