# Moscow Day of Week - Go Version

## Overview

A simple Go web server that displays the current day of the week in Moscow. The application returns the day in JSON format and updates in real-time with each request.

## Local Installation

1. Prerequisites
   - Go 1.21 or higher

2. Clone the repository

```bash
git clone <repository-url>
cd app_go
```

3. Run the application

```bash
go run main.go
```

4. Access the application
Open your browser or use curl to access: <http://localhost:8080>

The API will return JSON in the format:

```json
{
    "day_of_week": "Friday"
}
```

## Development

- Built with Go's standard library
- Uses built-in `net/http` package for HTTP server
- Uses `time` package for timezone handling
- Returns JSON response for easy integration
- No frontend, pure REST API
