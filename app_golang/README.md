# Go Web Application: Moscow Time API

This Go web application displays the current time in Moscow using the `net/http` package.

## Features

- Displays the current time in Moscow in the format `YYYY-MM-DD HH:MM:SS`
- Handles time zones using Go’s `time.LoadLocation`
- Built with Go standard `net/http` package

## Endpoints

### `GET /msc_time`

Returns the current time in Moscow.

**Response:**

```json
{
  "current_time_in_moscow": "2025-01-25 12:34:56"
}
```

## Installation

Follow the steps below to set up the application locally on your machine.

### 1. Clone the Repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/vtecovsky/S25-core-course-labs

cd app_golang
```

### 2. Install dependencies

```bash
go mod tidy
```

### 3. Running the Application

```bash
go run main.go
```

## Running in Docker container

### 1. Clone the Repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/vtecovsky/S25-core-course-labs
cd app_golang
```

### Build

```bash
docker build -t vtecovsky/app_golang:latest .
```

### Pull

```bash
docker pull vtecovsky/app_golang:latest
```

### Run

Start by cloning the repository to your local machine:

```bash
docker run -p 8080:8080 vtecovsky/app_golang:latest
```

# **CI Workflow** 🚀  

My **Continuous Integration (CI) pipeline** is designed to ensure code quality, reliability, and smooth deployment. The workflow is triggered whenever changes are made to the `app_go/` directory.

## **Pipeline Overview**  
The CI process consists of three key jobs:  

### 🔍 **1. Linting** 
- Uses **Golangci-lint** to enforce coding standards and detect potential issues.
- Ensures that the code follows Go best practices and is free from linting errors.

### 🧪 **2. Testing**
- Runs **Go test** to validate the correctness of the application.
- Ensures all tests pass before proceeding to the next stage.

### 📦 **3. Build & Push**
This step prepares and deploys the application using Docker:  
1. **Login** – Authenticates with Docker Hub.
2. **Build** – Creates a Docker image of the application.
3. **Push** – Uploads the built image to the container registry.

