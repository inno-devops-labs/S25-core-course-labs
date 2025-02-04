# Go Web Application: Guess the Number Game

![CI Status](https://github.com/creepydanunity/S25-core-course-labs/actions/workflows/ci.yml/badge.svg?branch=lab3)

## Overview
This is a simple web-based "Guess the Number" game built using the Gin framework. The server generates a random number between 1 and 100, and the user has to guess it. Feedback is provided on each guess.

## Features
- Generates a random number between 1 and 100.
- Provides feedback: "Too Low", "Too High", or "Correct".
- Resets the game after a correct guess.

## Installation

### Prerequisites
- Go 1.19 or later

### Steps
1. Clone the repository:
   ```bash
   git clone <your-repository-url>
   cd app_go

2. Install dependencies:
    ```bash
    go mod tidy

3. Run the application:
    ```bash
    go run main.go

4. Access at:
    http://localhost:8080

## Docker

### Build the container
```sh
docker build -t gin-mt .
```

### Run the container
```sh
docker run -p 8080:8080 gin-mt
```

### Run via Docker Hub
```sh
docker pull iucd/gin-mt:latest
docker run -p 8080:8080 iucd/gin-mt
```

## Distroless Image Version

### Build the container
```sh
docker build -t gin-mt:distroless -f distroless.Dockerfile .
```

### Run the container
```sh
docker run -p 8080:8080 gin-mt:distroless
```

### Run via Docker Hub
```sh
docker pull iucd/gin-mt:distroless
docker run -p 8080:8080 iucd/gin-mt:distroless
```

## Unit Tests
Unit tests have been implemented to ensure the correctness and reliability of the application. The tests cover the following key scenarios:

1. **Homepage Loading**:
   - Ensures the main page loads successfully with a valid HTTP response and contains the expected HTML structure.

2. **Invalid Input Handling**:
   - Tests form submission with a non-numeric guess to verify the application properly handles errors and returns an appropriate message.

3. **Guess Evaluation**:
   - Tests various numeric inputs to verify whether the server correctly responds with "Too Low", "Too High", or "Correct" feedback.

4. **Game Reset Mechanism**:
   - Ensures the game resets after a correct guess by verifying that the secret number changes.

### Running Tests
To execute the tests, use the following command:
```sh
go test ./...
```

## Continuous Integration (CI)
The project includes a GitHub Actions CI workflow to automate testing and Docker builds. The workflow consists of:

1. **Build and Test**:
   - Checks out the repository.
   - Sets up Go and installs dependencies.
   - Runs a linter for code quality checks.
   - Executes unit tests to validate functionality.

2. **Docker Build and Push**:
   - Logs in to Docker Hub using GitHub Secrets.
   - Builds the Docker image.
   - Pushes the images (original and distroless) to Docker Hub.

### Running CI Manually
The CI pipeline runs automatically on every push and pull request to the `main` branch. To trigger it manually, navigate to the GitHub Actions tab and run the workflow.