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

## Endpoints

- `/` - Displays the current date in Moscow as an HTML response using `/api/date` endpoint.
- `/api/date` - Returns the current date in Moscow as a JSON response.
