# Go Web Application - Daily Predictions

This is a simple Go web application that displays a random daily prediction every time the page is refreshed.

## Overview

The application uses Go's built-in `net/http` package to serve a lightweight and fast web application. Each time a user accesses the page, they are greeted with a random prediction for the day.

### Features

- Displays a random prediction on each page refresh.
- Lightweight and fast, built using Go's standard library.
- Scalable and easy to deploy.

---

## Installation and Running Locally

Follow the steps below to install and run the application locally:

### Prerequisites

- Go installed on your system (version 1.19+ recommended).

### Steps

1. Clone this repository:

   ```bash
   git clone https://github.com/Milanaaaa/S25-core-course-labs.git
   cd S25-core-course-labs/app_go
   ```

2. Build and run

   ``` bash
   go build -o main.out main.go
   ./main.out
   ```
