# Go Web Application: Moscow Time

This is a simple Go web application that displays the current time in Moscow, Russia. The application is built using the standard **net/http** package and follows best practices for Go web development.

---

## Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Running the Application](#running-the-application)
5. [Testing](#testing)
6. [Code Quality Checks](#code-quality-checks)
7. [Author](#author)

---

## Overview

The application serves a simple webpage displaying the current time in the Moscow timezone (`Europe/Moscow`). It utilizes **Go's standard library** for HTTP handling and time manipulation.

---

## Prerequisites

Before proceeding, ensure you have the following installed:

- **Go (1.18 or later)**: Download and install it from the official [Go website](https://go.dev/dl/).

---

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone git@github.com:Mohammed-Nour/S25-core-course-labs.git
   cd S25-core-course-labs/app_go
   ```

2. Install dependencies (if any are required):

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

- **Name**: Mohamad Nour Shahin
- **Email**: <mo.shahin@innopolis.university>

