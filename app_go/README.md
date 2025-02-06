# Go Web Application

This is a web application that displays the current time in Moscow using Gin.

## Run

   ```bash
   cd app_go
   ```
   ```bash
   go run main.go
   ```

Then go to http://localhost:8080/

## Docker

### Build

   ```bash
   cd app_go
   ```
   ```bash
   docker build -t go-web-app .
   ```

### Pull & Run

   ```bash
   docker pull netpo4ki/go-web:latest
   ```
   ```bash
   docker run -d -p 8000:8000 netpo4ki/go-web:latest
   ```
Then go to http://localhost:8080/


### Unit Tests
   ```bash
   cd app_go
   ```
   ```bash
   go test -v ./...
   ```

![CI Status](https://github.com/NetPo4ki/S25-core-course-labs/actions/workflows/ci.yml/badge.svg)