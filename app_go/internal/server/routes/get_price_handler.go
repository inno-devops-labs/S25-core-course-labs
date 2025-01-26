package routes

import (
	"encoding/json"
	"fmt"
	"github.com/labstack/echo/v4"
	"io"
	"net/http"
	"time"
)

const getPriceTimeout = 5 * time.Second

type PriceResponse struct {
	Pair        string `json:"pair"`
	Price       string `json:"price"`
	Change24h   string `json:"change_24h"`
	LastUpdated string `json:"last_updated"`
}

type TickerResponse struct {
	Symbol             string `json:"symbol"`
	LastPrice          string `json:"lastPrice"`
	PriceChangePercent string `json:"priceChangePercent"`
}

func GetPriceHandler(c echo.Context) error {
	client := &http.Client{Timeout: getPriceTimeout}

	// Fetch BTC/USDT data
	btcData, err := fetchPairData(client, "BTCUSDT")
	if err != nil {
		return c.JSON(http.StatusInternalServerError, map[string]string{
			"error": "failed to fetch BTC/USDT data",
		})
	}

	// Fetch ETH/USDT data
	ethData, err := fetchPairData(client, "ETHUSDT")
	if err != nil {
		return c.JSON(http.StatusInternalServerError, map[string]string{
			"error": "failed to fetch ETH/USDT data",
		})
	}

	resp := []PriceResponse{
		{
			Pair:        "BTC/USDT",
			Price:       btcData.LastPrice,
			Change24h:   btcData.PriceChangePercent,
			LastUpdated: time.Now().UTC().Format(time.RFC3339),
		},
		{
			Pair:        "ETH/USDT",
			Price:       ethData.LastPrice,
			Change24h:   ethData.PriceChangePercent,
			LastUpdated: time.Now().UTC().Format(time.RFC3339),
		},
	}

	return c.JSON(http.StatusOK, resp)
}

func fetchPairData(client *http.Client, symbol string) (*TickerResponse, error) {
	url := fmt.Sprintf("https://api.binance.com/api/v3/ticker/24hr?symbol=%s", symbol)
	resp, err := client.Get(url)
	if err != nil {
		return nil, fmt.Errorf("client.Get failed: %w", err)
	}
	defer resp.Body.Close()

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return nil, fmt.Errorf("io.ReadAll failed: %w", err)
	}

	var data TickerResponse
	err = json.Unmarshal(body, &data)
	if err != nil {
		return nil, fmt.Errorf("json.Unmarshal failed: %w", err)
	}

	if data.Symbol == "" {
		return nil, fmt.Errorf("invalid response for symbol %s", symbol)
	}

	return &data, nil
}
