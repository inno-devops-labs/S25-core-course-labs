# Go Web Application

## 📘 Overview

This is a simple web application that is built using Go and Gin to calculate person's age by their date of birth!

![Main page of the application](media/overview.png)

---

## 💻 Local Installation

### Prerequisites

The project requires you to have:

- go 1.23.5
- make (optional, just directly run the commands inside `Makefile`, if it is not available)

### Installation Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/MagicWinnie/S25-core-course-labs
   git checkout lab1
   cd S25-core-course-labs/app_go
   ```

2. Install the dependencies:

   ```bash
   go mod download
   ```

3. Run the application:

   ```bash
   make run
   ```

4. Navigate to <http://127.0.0.1:8080>.

---

## 🐳 Docker

### Distro-based Image Version

Containerized version of the web application:

- uses Alpine version of Go 1.23.5;
- installs the application in `/app` directory;
- creates a nonroot user `user`;
- runs the application on port `8080`.

#### How to build?

   ```bash
   # clone the repository
   git clone https://github.com/MagicWinnie/S25-core-course-labs
   git checkout lab2
   cd S25-core-course-labs/app_go
   # build the image
   docker build -t simple-go-web-app .
   # run a container
   docker run -p 8888:8080 simple-go-web-app
   ```

#### How to pull?

   ```bash
   docker pull magicwinnie/simple-go-web-app:latest
   ```

#### How to run?

   ```bash
   docker run -p 8888:8080 magicwinnie/simple-go-web-app:latest
   ```

### Distroless Image Version

Containerized version of the web application:

- uses `golang:1.23.5-alpine3.21` and `gcr.io/distroless/static-debian12:nonroot`;
- installs the application in `/app` directory;
- uses a nonroot tag;
- runs the application on port `8080`.

#### How to build?

   ```bash
   # clone the repository
   git clone https://github.com/MagicWinnie/S25-core-course-labs
   git checkout lab2
   cd S25-core-course-labs/app_go
   # build the image
   docker build -t simple-go-web-app-distroless -f distroless.Dockerfile .
   # run a container
   docker run -p 8888:8080 simple-go-web-app-distroless
   ```

#### How to pull?

   ```bash
   docker pull magicwinnie/simple-go-web-app-distroless:latest
   ```

#### How to run?

   ```bash
   docker run -p 8888:8080 magicwinnie/simple-go-web-app-distroless:latest
   ```

---

## 🛠️ Development

- These tools are required:

  - [golangci-lint](https://golangci-lint.run/welcome/install/)
  - [gofumpt](https://github.com/mvdan/gofumpt)

- Format the code:

   ```bash
   make format
   ```

- Statically check the code using golangci-lint and gofumpt:

   ```bash
   make check
   ```

- Build the application:

    ```bash
    make build
    ```
