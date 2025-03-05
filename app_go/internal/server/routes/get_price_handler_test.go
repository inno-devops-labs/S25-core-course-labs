package routes

import (
	"app_go/internal/http_client"
	mock_http_client "app_go/internal/mocks"
	"io"
	"net/http"
	"net/http/httptest"
	"strings"
	"testing"

	"github.com/labstack/echo/v4"
	"github.com/stretchr/testify/assert"
	"go.uber.org/mock/gomock"
)

func TestGetPriceHandler(t *testing.T) {
	ctrl := gomock.NewController(t)
	defer ctrl.Finish()

	e := echo.New()

	mockClient := mock_http_client.NewMockHTTPClient(ctrl)

	t.Run(
		"success", func(t *testing.T) {
			btcResponse := &http.Response{
				StatusCode: http.StatusOK,
				Body:       io.NopCloser(strings.NewReader(`{"symbol":"BTCUSDT","lastPrice":"45000.00","priceChangePercent":"1.5"}`)),
			}

			ethResponse := &http.Response{
				StatusCode: http.StatusOK,
				Body:       io.NopCloser(strings.NewReader(`{"symbol":"ETHUSDT","lastPrice":"3000.00","priceChangePercent":"2.1"}`)),
			}

			mockClient.EXPECT().
				Get("https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT").
				Return(btcResponse, nil)
			mockClient.EXPECT().
				Get("https://api.binance.com/api/v3/ticker/24hr?symbol=ETHUSDT").
				Return(ethResponse, nil)

			handler := GetPriceHandler(http_client.New(mockClient))

			req := httptest.NewRequest(http.MethodGet, "/price", nil)
			rec := httptest.NewRecorder()
			c := e.NewContext(req, rec)

			if assert.NoError(t, handler(c)) {
				assert.Equal(t, http.StatusOK, rec.Code)
			}
		},
	)

	t.Run(
		"error fetching BTC", func(t *testing.T) {
			mockClient.EXPECT().
				Get("https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT").
				Return(nil, assert.AnError)

			handler := GetPriceHandler(http_client.New(mockClient))

			req := httptest.NewRequest(http.MethodGet, "/price", nil)
			rec := httptest.NewRecorder()
			c := e.NewContext(req, rec)

			if assert.NoError(t, handler(c)) {
				assert.Equal(t, http.StatusInternalServerError, rec.Code)
			}
		},
	)
}
