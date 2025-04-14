# Go Web Application: Moscow Time Documentation

## Framework Choice: net/http

I chose the **net/http** package for this web application because it is the standard library for building web applications in Go. It is lightweight, efficient, and provides full control over HTTP handling without requiring external dependencies. This makes it ideal for simple and performant web applications.

---

## Best Practices Applied

### 1. **Efficient Template Handling**

- Templates are parsed once at startup using `template.Must(template.ParseFiles(...))`, reducing redundant parsing during each request.
- The `html/template` package is used to prevent XSS attacks by safely escaping user input.

### 2. **Logging for Debugging**

- The `log` package is used for logging errors, making it easier to debug issues such as template rendering failures or HTTP server errors.

### 3. **Separation of Concerns**

- The logic to fetch the Moscow time is placed in a separate function (`showCurrentTimeMoscow`) for better modularity.
- The `PageData` struct is defined globally to maintain structured data for templates.

### 4. **Proper Error Handling**

- All potential errors, such as time zone loading and template execution failures, are handled gracefully to prevent crashes.

### 5. **Static Code Analysis & Linting**

- The code adheres to Go best practices and is checked with `golangci-lint` for compliance with Go coding standards.

---

## Testing

To ensure the application works correctly, the following steps were taken:

### **1. Static Code Analysis**

```bash
golangci-lint run
go vet
```

### **2. Dependency Installation**

```bash
go mod tidy
```

### **3. Unit Testing**

Unit tests were created to validate the functionality of the application. The tests are organized into separate files and cover the following scenarios.

#### **Best Practices Applied in Unit Tests**

1. **Clear and Descriptive Test Names**:
   - Test functions and files are named descriptively to reflect their purpose (e.g., `h1_tag_exist_test.go`, `time_accuracy_test.go`).

2. **Isolated Tests**:
   - Each test is independent and does not rely on the state of other tests. This ensures that tests can be run in any order and still produce consistent results.

3. **Helper Functions**:
   - Helper functions are used to avoid code duplication and improve readability.

4. **Descriptive Error Messages**:
   - Descriptive error messages are included in assertions to make it easier to diagnose failures.

5. **Edge Case Handling**:
   - Tests include error handling for edge cases, such as incorrect time formats or missing elements in the response.

6. **Modular Test Structure**:
   - Tests are organized into separate files, each focusing on a specific aspect of the application.

#### **Test Files**

##### **a. `h1_tag_exist_test.go`**

- **Purpose**: Verifies that the response contains an `<h1>` tag displaying the current Moscow time.
- **Best Practices**:
  - Uses `strings.Contains` to check for the `<h1>` tag.
  - Includes a descriptive error message if the tag is missing.

##### **b. `home_route_test.go`**

- **Purpose**: Ensures that the home route (`/`) returns a 200 status code.
- **Best Practices**:
  - Uses `httptest.NewRecorder` to simulate an HTTP request.
  - Includes a descriptive error message for failed assertions.

##### **c. `time_accuracy_test.go`**

- **Purpose**: Validates that the time displayed on the page matches the current time in Moscow.
- **Best Practices**:
  - Uses `time.LoadLocation("Europe/Moscow")` to get the correct Moscow time.
  - Compares the displayed time with the actual time to check for accuracy.
  - Includes a descriptive error message if the times do not match.

##### **d. `time_format_test.go`**

- **Purpose**: Ensures that the time displayed on the page follows the expected format (`HH:MM:SS`).
- **Best Practices**:
  - Uses `time.Parse("15:04:05", timeString)` to validate the format.
  - Includes error handling and a descriptive error message for failed assertions.

### **4. Manual Testing**

- The application was run locally, and the displayed time was verified to match the current time in Moscow.
- The page was refreshed multiple times to confirm that the time updates correctly.

### **5. Running the Web Application**

```bash
go run app.go
```

---

## Code Quality

The application follows best practices for code quality, including:

- Proper documentation and comments within the code.
- Separation of logic into reusable functions.
- Logging for debugging and error handling.
- Static code analysis and linting using `golangci-lint`.
