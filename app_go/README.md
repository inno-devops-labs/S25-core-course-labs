# Go Web Application: Moscow Time

This is a simple Go web application that displays the current time in Moscow, Russia. The application is built using the standard **net/http** package and follows best practices for Go web development.

---

## Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Running the Application](#running-the-application)
5. [Testing](#testing)
6. [Docker](#docker)
7. [Distroless Image Version](#distroless-image-version)
8. [Code Quality Checks](#code-quality-checks)
9. [Author](#author)

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
git clone git@github.com:Ali12hamdan/S25-core-course-labs.git
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

## Docker

This application is containerized using Docker, following best practices for building and running Docker images.

### How to Build the Docker Image

1. Navigate to the `app_go` directory:

   ```bash
   cd S25-core-course-labs/app_go
   ```

2. Build the Docker image:

   ```bash
   docker build -t ali12hamdan/app_go:app_go-prod-1.0.0 --no-cache=True .
   ```

   - The `--no-cache=True` flag ensures a clean build by ignoring cached layers.

### How to Run the Docker Image

1. Run the Docker container:

   ```bash
   docker run -d -p 3000:3000 --name app_go ali12hamdan/app_go:app_go-prod-1.0.0
   ```

2. Access the application at `http://localhost:3000`.

### How to Push the Docker Image to Docker Hub

1. Log in to Docker Hub (if not already logged in):

   ```bash
   docker login
   ```

2. Push the Docker image:

   ```bash
   docker push ali12hamdan/app_go:app_go-prod-1.0.0
   ```

### How to Pull the Docker Image from Docker Hub

1. Pull the Docker image:

   ```bash
   docker pull ali12hamdan/app_go:app_go-prod-1.0.0
   ```

2. Run the container as described in the "How to Run the Docker Image" section.

---

## Distroless Image Version

This application is also available in a **Distroless** version, which is a minimal Docker image that only includes the application and its runtime dependencies, without unnecessary tools or package managers.

### How to Build the Distroless Docker Image

1. Navigate to the `app_go` directory:

   ```bash
   cd S25-core-course-labs/app_go
   ```

2. Build the Distroless Docker image:

   ```bash
   docker build -t ali12hamdan/app_go:app_go-distroless-prod-1.0.0 --file distroless.Dockerfile --no-cache=True .
   ```

   - The `--file distroless.Dockerfile` flag specifies the custom Dockerfile for the Distroless build.
   - The `--no-cache=True` flag ensures a clean build by ignoring cached layers.

### How to Run the Distroless Docker Image

1. Run the Distroless Docker container:

   ```bash
   docker run -d -p 3000:3000 --name app_go_distroless ali12hamdan/app_go:app_go-distroless-prod-1.0.0
   ```

2. Access the application at `http://localhost:3000`.

### How to Push the Distroless Docker Image to Docker Hub

1. Log in to Docker Hub (if not already logged in):

   ```bash
   docker login
   ```

2. Push the Distroless Docker image:

   ```bash
   docker push ali12hamdan/app_go:app_go-distroless-prod-1.0
   ```

### How to Pull the Distroless Docker Image from Docker Hub

1. Pull the Distroless Docker image:

   ```bash
   docker pull ali12hamdan/app_go:app_go-distroless-prod-1.0
   ```

2. Run the container as described in the "How to Run the Distroless Docker Image" section.

---

## Code Quality Checks

To ensure the code adheres to best practices and Go coding standards, the following tools are used:

### 1. **Gofmt** (Code Formatting)

   `gofmt` ensures that the code follows Go's standard formatting rules.

   ```bash
   gofmt -l .
   ```

   > **Note**: To automatically format your code, run:

   ```bash
   gofmt -w .
   ```

### 2. **Golint** (Static Code Analysis)

   `golint` analyzes the code for style mistakes and best practices.

   ```bash
   golint ./...
   ```

### 3. **Go Vet** (Error Detection)

   `go vet` examines the code for common mistakes.

   ```bash
   go vet ./...
   ```

---

## Author

- **Name**: Ali Hamdan
- **Email**: <al.hamdan@innopolis.university>
