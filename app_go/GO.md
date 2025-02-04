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

1. **Static Code Analysis**:

   ```bash
   golangci-lint run
   go vet
   ```

2. **Dependency Installation**:

   ```bash
   go mod tidy
   ```

3. **Manual Testing**:
   - The application was run locally, and the displayed time was verified to match the current time in Moscow.
   - The page was refreshed multiple times to confirm that the time updates correctly.

4. **Running the Web Application**:

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
