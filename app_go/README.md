# Crypto Price Tracker

Web application that provides real-time cryptocurrency prices in JSON format using Binance API.

## Features

- Get BTC/USDT and ETH/USDT prices with 24h changes
- RESTful JSON API
- `Makefile` with commands to run, test and build the application
- Environment configuration via `.env`

## Installation

### Prerequisites

- Go 1.20+
- Make

### Local Setup

1. Clone repository:

```bash
git clone https://github.com/nikitashlyahktin/S25-core-course-labs
cd S25-core-course-labs/app_go
```

1. Install dependencies:

```bash
go mod download
# Installs Echo, godotenv, etc.
```

1. Build and run:

```bash
make run
# Server starts on http://localhost:8080
```

## Usage

Access the API endpoint:

```bash
curl http://localhost:8080/price
```

### Example Response

```json
[
  {
    "pair": "BTC/USDT",
    "price": "104686.77000000",
    "change_24h": "0.237",
    "last_updated": "2025-01-26T11:27:17Z"
  },
  {
    "pair": "ETH/USDT",
    "price": "3307.87000000",
    "change_24h": "0.461",
    "last_updated": "2025-01-26T11:27:17Z"
  }
]
```

## Project Structure

```txt
.
├── cmd/
│   └── api/             # Main application
├── internal/
│   └── server/          # Server setup
├── Makefile             # Build commands
└── .env                 # Environment variables
```

## Testing

1. Start server: `make run`

2. Access the API endpoint with a web browser: `http://localhost:8080/price`

## Documentation

See [GO.md](GO.md) for technical implementation details
