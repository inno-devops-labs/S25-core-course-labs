# Go Numerology application

## Overview

This web application returns a random fact about a randomly generated number.

## Installation and running

```bash
# Installing the repo itself
git clone https://github.com/m0t9/S25-core-course-labs -b lab1

# Download dependencies
cd S25-core-course-labs/app_go
go mod download

# Running application
cd cmd/numerologist
go run main.go

# Testing
curl http://127.0.0.1:8080
```

## Docker

### Build

```bash
cd S25-core-course-labs/app_go
docker build -f Dockerfile -t goapp .
```

### Pull & Run

```bash
# Pulling the image
docker pull m0t9docker/goapp:latest

# Running the container
docker run -d -p 8000:8080 m0t9docker/goapp:latest

# Testing
curl http://127.0.0.1:8000
```

### Distroless Image Version

#### Build

```bash
cd S25-core-course-labs/app_go
docker build -f distroless.Dockerfile -t goapp_distro .
```

#### Pull & Run

```bash
# Pulling the image
docker pull m0t9docker/goapp_distro:latest

# Running the container
docker run -d -p 8000:8080 m0t9docker/goapp_distro:latest

# Testing
curl http://127.0.0.1:8000
```
