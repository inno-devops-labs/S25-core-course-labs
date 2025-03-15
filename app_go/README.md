# Go Web Application: Random Motivation Quotes

## Project Overview

This Go web application is designed to display a random motivational quote on each page refresh. The application is built using the **Gin** framework, known for its speed and minimalist design, enabling rapid development while adhering to modern coding standards.

## Technologies used

- **Gin:** a lightweight and fast web framework for Go, providing essential tools for creating efficient and reliable web applications.
- **math/rand:** a Go package for generating pseudo-random numbers, used to select a random quote from a predefined list.

## Features

1. **Dynamic Quote Generation:**
The application displays a random motivational quote every time the page is refreshed.
2. **Minimalistic Design:**
The application focuses on simplicity and speed with clean and modular code.
3. **JSON Response:**
Quotes are returned in a structured JSON format, making the application extensible and easy to integrate with other systems.

## Installation and Usage

Clone the repository:

```bash
git clone https://github.com/Pupolina7/S25-core-course-labs.git
```

Navigate to the folder:

```bash
cd S25-core-course-labs/app_go/
```

Install Go dependencies:

```bash
 go mod init app.go
```

Download the **Gin** framework dependency:

```bash
 go get -u github.com/gin-gonic/gin
```

Run the application locally:

```bash
go run main.go
```

Go to localhost:

```bash
http://localhost:8080
```
