# Moscow Date Web-Application

## About

This is a simple web application on Go that displays the current date in Moscow.

## How to Use

### Manual

1. Run the application using the following command:

```bash
go run main.go
```

2. Open your web browser and navigate to `http://0.0.0.0:8002/` to view the current date in Moscow.

### Regular Docker Image

1. Build or pull the Docker image.

- Build the Docker image using the following command:

```bash
docker build -t azamatbayramov/s25-devops-go .
```

- Pull the Docker image from Docker Hub using the following command:

```bash
docker pull azamatbayramov/s25-devops-go
```

2. Run the Docker container using the following command:

```bash
docker run -p 8002:8002 azamatbayramov/s25-devops-go
```

3. Open your web browser and navigate to `http://0.0.0.0:8002/` to view the current date in Moscow.

### Distroless Docker Image

1. Build or pull the Docker image.

- Build the Docker image using the following command:

```bash
docker build -t azamatbayramov/s25-devops-go-dl -f distroless.Dockerfile .
```

- Pull the Docker image from Docker Hub using the following command:

```bash
docker pull azamatbayramov/s25-devops-go-dl
```

2. Run the Docker container using the following command:

```bash
docker run -p 8002:8002 azamatbayramov/s25-devops-go-dl
```

3. Open your web browser and navigate to `http://0.0.0.0:8002/` to view the current date in Moscow.

## Unit Tests

1. Run the unit tests using the following command:

```bash
go test ./...
```

## CI Workflow

The CI workflow for this application is defined in the `.github/workflows/app_go.yml` file.

It consists of the following steps:
- **Build and Test**:
    - Sets up the Go environment.
    - Lints the code using `go fmt`.
    - Runs the unit tests using `go test`.
    - Scans for vulnerabilities using Snyk.
- **Build and Push**:
    - Sets up Docker Buildx.
    - Logs in to Docker Hub.
    - Builds and pushes the Docker image using the distroless Dockerfile.

## Endpoints

- `/` - Displays the current date in Moscow as an HTML response using `/api/date` endpoint.
- `/api/date` - Returns the current date in Moscow as a JSON response.
