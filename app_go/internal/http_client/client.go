package http_client

import (
	"net/http"
)

type HTTPClient interface {
	Get(url string) (*http.Response, error)
}

type Client struct {
	HTTPClient
}

func New(httpClient HTTPClient) *Client {
	return &Client{httpClient}
}
