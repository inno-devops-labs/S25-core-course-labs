# Crypto Price Tracker

![CI](https://github.com/nikitashlyahktin/S25-core-course-labs/actions/workflows/go-app.yml/badge.svg)

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

## Docker

Docker helps to run the application without managing application dependencies by yourself.

You can either build your own docker image from `Dockerfile` or use prebuilt image from docker hub.
Then you can run the container and use the app.

### Docker Prerequisites

- Docker engine (e.g. Docker Desktop or Colima) installed and running

### Build Image

Use the following command in `app_go` directory to build the image from `Dockerfile`:

```bash
docker build -t crypto_price_tracker .
```

### Pull Prebuilt Image

Use the following command to pull prebuilt image from docker hub:

```bash
docker pull nshlyakhtin/devops:lab2_app_go
```

### Run Container

```bash
docker run -p 8080:8080 crypto_price_tracker
# or for prebuilt image:
docker run -p 8080:8080 nshlyakhtin/devops:lab2_app_go
```

## Distroless Image Version

You can use smaller and more secure distroless docker image for running the application

### Build Distroless Image

Use the following command in `app_go` directory to build the image from `distroless.Dockerfile`:

```bash
docker build -f distroless.Dockerfile -t crypto_price_tracker_distroless .
```

### Pull Prebuilt Distroless Image

Use the following command to pull prebuilt image from docker hub:

```bash
docker pull nshlyakhtin/devops:lab2_app_go_distroless
```

### Run Container With Distroless Image

```bash
docker run -p 8080:8080 crypto_price_tracker_distroless
# or for prebuilt image:
docker run -p 8080:8080 nshlyakhtin/devops:lab2_app_go_distroless
```

## Example Response

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

## Unit Tests

This application supports Unit Tests.

Run Unit Tests using following command:

```bash
make test
```

## Continuous Integration (CI)

This project uses GitHub Actions to automate testing and deployment.

### CI Workflow Steps

1. Install Dependencies: The workflow installs all required dependencies from `requirements.txt`.
2. Run Linter: The `black` linter checks the code formatting.
3. Run Tests: Unit tests are executed with `pytest`.
4. Docker Login, Build & Push: The application is built as a Docker image and pushed to Docker Hub.

Full CI config is located at `.github/workflows/go-app.yml`.
