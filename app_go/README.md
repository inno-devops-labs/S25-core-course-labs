# Go Web Application: Greeting Handler

This Go web application provides a simple endpoint to greet a person by name. The response is returned in JSON format and defaults to greeting "Guest" if no name is provided.

## Features

- Accepts a `name` query parameter via the `/greet` endpoint.
- Returns a JSON response with the structure: `{ "greeting": "Hello, <name>! Welcome!" }`.
- Defaults to greeting "Guest" if the `name` parameter is not provided.

## Getting Started

### Prerequisites

1. Install [Go](https://go.dev/dl/) (version 1.16 or later).

### Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Initialize and tidy the Go module:

   ```bash
   go mod tidy
   ```

3. Build and run the application:

   ```bash
   go run main.go
   ```

### Running the Application

1. Start the server:

   ```bash
   go run main.go
   ```

2. Access the application:
   - With a name: `http://localhost:8000/greet?name=John`
   - Without a name: `http://localhost:8000/greet`

### Example cURL Commands

- **With a name**:

  ```bash
  curl -X GET "http://localhost:8000/greet?name=John" -H "Accept: application/json"
  ```

- **Without a name**:

  ```bash
  curl -X GET "http://localhost:8000/greet" -H "Accept: application/json"
  ```

### Expected Outputs

- With name:

  ```json
  { "greeting": "Hello, John! Welcome!" }
  ```

- Without name:

  ```json
  { "greeting": "Hello, Guest! Welcome!" }
  ```

## Project Structure

```bash
.
├── main.go               # Main application file
├── go.mod                # Go module
├── main_test.go          # Unit tests for the handler
└── README.md             # Project documentation
```

## Testing

1. To run the unit tests:

   ```bash
   go test
   ```

2. The test verifies:
   - The correct greeting is returned when a name is provided.
   - The default greeting is returned when no name is provided.
