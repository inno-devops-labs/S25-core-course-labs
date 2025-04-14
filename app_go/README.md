## Overview
A simple web application that displays the current time in Innopolis.

## Start
1) Clone current project;
2) Start the server: `go run main.go`
3) Checkout `http://localhost:8080`

##  Distroless Image
Used for:
- Reducing the size of the image.
- Eliminateing unnecessary packages.
- Running the application with a `non-root` user.

## Go CI/CD
Automatically performs:
- Install dependencies.
- Run tests `go test`.
- Build and publish Docker image to Docker Hub.

## Go CI Status
![Go CI](https://github.com/AlexeyKureykin/S25-core-course-labs/actions/workflows/ci-go.yml/badge.svg)
