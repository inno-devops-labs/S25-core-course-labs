# Go Web Application: Moscow Time

This is a simple Go web application that displays the current time in Moscow, Russia. The application is built using the standard **net/http** package and follows best practices for Go web development.

---

[![Go Web Application (Moscow Time)](https://github.com/Mohammed-Nour/S25-core-course-labs/actions/workflows/go-app.yml/badge.svg)](https://github.com/Mohammed-Nour/S25-core-course-labs/actions/workflows/go-app.yml)

## Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Running the Application](#running-the-application)
5. [Testing](#testing)
6. [Unit Tests](#unit-tests)
7. [Docker](#docker)
8. [Distroless Image Version](#distroless-image-version)
9. [CI Workflow](#ci-workflow)
10. [Code Quality Checks](#code-quality-checks)
11. [Author](#author)

---

## Overview

The application serves a simple webpage displaying the current time in the Moscow timezone (`Europe/Moscow`). It utilizes **Go's standard library** for HTTP handling and time manipulation.

---

## Prerequisites

Before proceeding, ensure you have the following installed:

- **Go (1.18 or later)**: Download and install it from the official [Go website](https://go.dev/dl/).

---

## Installation

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone git@github.com:Mohammed-Nour/S25-core-course-labs.git
cd S25-core-course-labs/app_go
```

### 2. Install Dependencies

Ensure all dependencies are installed:

```bash
go mod tidy
```

---

## Running the Application

1. Start the server:

   ```bash
   go run app.go
   ```

2. Open your browser and navigate to `http://localhost:3000/`.

   > **Note**: The server will start listening on port `3000`. You can stop the server by pressing `Ctrl+C` in the terminal.

---

## Testing

To ensure the application works correctly:

1. Run the application and verify that the displayed time matches the current time in Moscow.
2. Refresh the page to confirm that the time updates dynamically.
3. Check the server logs for any errors.

---

## Unit Tests

Unit tests have been implemented to validate the functionality of the application. These tests ensure that the application behaves as expected and adheres to best practices. The tests are written using the `testing` package and cover the following scenarios:

- **Home Route**: Ensures the home route (`/`) returns a 200 status code.
- **Response Body**: Verifies that the response contains the expected HTML structure displaying the current time.
- **Time Accuracy**: Validates that the time displayed on the page matches the current time in Moscow.
- **Time Format**: Ensures the time is displayed in the correct format (`HH:MM:SS`).
- **Timezone**: Verifies that the time is correctly localized to the Moscow timezone.

### Running Unit Tests

To run the unit tests, execute the following command:

```bash
go test ./...
```

> **Note**: Ensure the application is correctly set up before running the tests.

---

## Docker

This application is containerized using Docker, following best practices for building and running Docker images.

### How to Build the Docker Image

```bash
docker build -t oshaheen1882051/app_go:app_go-prod-1.0.0 --no-cache=True .
```

### How to Run the Docker Image

```bash
docker run -d -p 3000:3000 --name app_go oshaheen1882051/app_go:app_go-prod-1.0.0
```

---

## Distroless Image Version

A **Distroless** version is available, which includes only the application and runtime dependencies.

### How to Build the Distroless Docker Image

```bash
docker build -t oshaheen1882051/app_go:app_go-distroless-prod-1.0.0 --file distroless.Dockerfile --no-cache=True .
```

### How to Run the Distroless Docker Image

```bash
docker run -d -p 3000:3000 --name app_go_distroless oshaheen1882051/app_go:app_go-distroless-prod-1.0.0
```

---

## CI Workflow  

This repository uses **GitHub Actions** to automate the **build, test, and deployment** processes. The workflow ensures code quality, security, and efficient deployment.  

### **Trigger Conditions**  

The workflow runs on:  

- **Push events** to the `lab3` and `master` branches when changes occur in the `app_go` folder.  
- **Pull requests** targeting the `master` branch, filtered to changes in the `app_go` folder.  

### **Workflow Jobs**  

The CI pipeline consists of the following key jobs:  

1. **Security**  
   - Runs **Snyk vulnerability checks** to detect and report known security issues.  

2. **Build & Test**  
   - Installs **Go modules** and project dependencies.  
   - Performs **code linting** using **golangci-lint**.  
   - Runs **unit tests** with **go test**, including coverage reporting.  

3. **Docker**  
   - Logs in to **Docker Hub**.  
   - Sets up the necessary **build environment** with **QEMU** and **Docker Buildx**.  
   - Builds and pushes both a **standard Docker image** and a **distroless version** for enhanced security.  

### **Efficiency and Best Practices**  

- Utilizes **caching** for **Go modules** and **Docker layers** to improve build performance.  
- **Snyk integration** ensures continuous security monitoring.  
- A **status badge** at the top of the README provides quick visibility into the latest build status.  
  
---

## Code Quality Checks

### 1. **Gofmt** (Code Formatting)

```bash
gofmt -l .
```

To automatically format your code:

```bash
gofmt -w .
```

### 2. **Golint** (Static Code Analysis)

```bash
golint ./...
```

### 3. **Go Vet** (Error Detection)

```bash
go vet ./...
```

---

## Author

- **Name**: Mohamad Nour Shahin
- **Email**: <mo.shahin@innopolis.university>