package metrics

import (
	"github.com/prometheus/client_golang/prometheus"
)

var PriceRequestCounter = prometheus.NewCounter(
	prometheus.CounterOpts{
		Name: "price_request_total",
		Help: "Total number of requests to the /price endpoint",
	},
)

func init() {
	prometheus.MustRegister(PriceRequestCounter)
}
