# Random joke web application

## Overview

This web application displays a random joke from the [public API](https://jokeapi.dev/). It supports two formats of the output:

- Web page containing a random joke
- JSON with random joke

The Swagger documentation is available at the following path: `/swagger/index.html`.

## Tools

- [Gin](https://github.com/gin-gonic/gin)
- [net/http](https://pkg.go.dev/net/http)
- [time](https://pkg.go.dev/time)
- [staticcheck](https://staticcheck.dev/)
- [gofmt](https://pkg.go.dev/cmd/gofmt)

## Installation

```bash
# 1. Clone the repository
git clone https://github.com/danmaninc/S25-core-course-labs

# 2. Change directory
cd S25-core-course-labs/app_golang

# 3. Install the dependencies
go mod download

# 4. Build the application
go build src/main.go

# 5. Run the application
./main

# 6. Test the application
curl http://localhost
curl http://localhost/joke
```

## Docker

### How to build?

You can build the Docker image using the following command:

```bash
docker build app_golang -t app_golang
```

### How to pull?

To pull the latest image from Docker Hub, use the following command:

```bash
docker pull dnworks/app_golang:latest
```

### How to run?

Run the Docker container:
> **NB!** Port 80 must be exposed so you can access the web application at 80 port (`http://localhost/`).

- Self-built image:

```bash
docker run -p 80:80 app_golang
```

- From Docker Hub:

```bash
docker run -p 80:80 dnworks/app_golang:latest
```

## Distroless Image Version

### How to build?

```bash
docker build -f app_golang/distroless.Dockerfile app_golang -t app_golang_dstlss
```

### How to pull?

```bash
docker pull dnworks/app_golang_dstlss:latest
```

### How to run?

> **NB!** Port 80 must be exposed so you can access the web application at 80 port (`http://localhost/`).

- Self-built image:

```bash
docker run -p 80:80 app_golang_dstlss
```

- From Docker Hub:

```bash
docker run -p 80:80 dnworks/app_golang_dstlss:latest
```
