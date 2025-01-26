# Moscow Date Web-Application

## About

This is a simple web application on Go that displays the current date in Moscow.

## How to Use

1. Run the application using the following command:

```bash
go run main.go
```

2. Open your web browser and navigate to `http://0.0.0.0:8002/` to view the current date in Moscow.

## Endpoints

- `/` - Displays the current date in Moscow as an HTML response using `/api/date` endpoint.
- `/api/date` - Returns the current date in Moscow as a JSON response.
