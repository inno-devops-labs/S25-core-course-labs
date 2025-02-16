# Framework Choice: net/http

**Justification for Choosing net/http:**

1. **Ease of Use:** It's the simplest built-in framework.
2. **Template Support:** Uses net/templates to support SSR.

This framework aligns with the project's needs for simplicity, efficiency, and maintainability.


# Best Practices and Coding Standards

This document outlines the best practices and coding standards followed in the development of the **Fork Counter Web Application**.

---

## **Best Practices Applied**

### 1. **Code Structure and Organization**
- The application follows a modular structure:
  - `main.go`: Contains the WEB application logic.
  - `templates/`: Stores HTML templates for rendering the frontend.

### 2. **Environment Management**
- There are no external dependencies.

### 3. **Error Handling**
- All errors are handled and logged.

### 4. **Security**
- net/http includes built-in security features like data validation and protection against common vulnerabilities (e.g., SQL injection, XSS).

### 5. **Performance**
- Asynchronous programming is used to handle multiple requests efficiently.

### 6. **Documentation**
- The application is documented in `README.md` and `GO.md`.

### 7. **Coding Standards**
- Code follows guidelines for readability and consistency.

### 8. **Version Control**
- A `.gitignore` file is maintained to exclude unnecessary files.

### 9. **Testing**
- Manual testing was applied, I checked page refresh and tried to break the counter.

---

## **Dependencies**
No external dependencies.

# Unit Tests
## Test File Structure

- **`integration_test.go`**: Contains the unit tests for the application's endpoint.

## Unit Tests Created

1. **`TestMainServerIntegration`**:
  - **Purpose**: Verify that the GET request to the root endpoint (`"/"`) returns an HTTP 200 status code and content are rendered.
  - **Best Practice**: Ensures that the endpoint is reachable and responds as expected.

