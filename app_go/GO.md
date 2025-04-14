# Moscow Time Web Application
This Go web application demonstrates the use of best practices for building a small, maintainable, and efficient web app.

# Frameworks Used
## Go (Golang):
Go is a statically typed, compiled programming language designed for simplicity, concurrency, and performance. It's ideal for web applications like this due to its lightweight nature, speed, and ease of deployment. It also has a powerful standard library with built-in support for HTTP, making it an excellent choice for small web apps.

# Project Structure
```
app_go/
│
├── index.html
│── app.go
├── GO.md
├── README.md
└── .gitignore

```

# Coding Standards

1. **Go Code Style::**
   - Followed Go's best practices for code formatting, which includes using the gofmt tool to ensure consistent formatting across the codebase.
   - Used clear and descriptive variable names such as moscowTime and formattedTime to maintain readability.

2. **Error Handling:**
   - Go emphasizes explicit error handling. All errors are caught and returned to the user to avoid any unexpected crashes.
   - Used http.Error() to handle API errors and gracefully display them in case of issues.

3. **Secure and Performant Code:**
   - Limited the API request timeout to avoid hanging indefinitely if the server is unresponsive.
   - Included error checks when parsing the JSON response and handling HTTP errors to ensure reliability.

# Testing and Debugging

1. **Manual Testing:**
   - Tested the Go web app locally to ensure that:
     - The API integration works correctly.
     - Errors are displayed in case of issues (e.g., slow internet connection or invalid API response).
     - The rendered HTML template is properly updated with the correct time.

2. **Error Handling:**
   - Used explicit error checking ```(if err != nil)``` to catch and display errors.
   - Fallback behavior is included in case of API failures, such as showing an error message on the page.

# Code Quality

1. **Dependencies:**
   - Go projects don't use a ```requirements.txt``` file like Python. Instead, Go modules ```(go.mod)``` are used to manage dependencies. The necessary dependencies for this project are automatically fetched when running ```go run```.


2. **HTML Integration:**
   - Followed semantic HTML practices in index.html for accessibility and clarity.
   - The styling uses CSS for a responsive and visually appealing UI design, leveraging animations for dynamic effects.
