# 🎉 Random Programming Quote Generator (Go)

![Go Version](https://img.shields.io/badge/Go-1.20%2B-blue.svg)
![CI/CD Pipeline](https://github.com/Azaki-san/S25-core-course-labs/actions/workflows/app_golang_ci.yml/badge.svg)

🌟 **A fun and inspirational app!**

---

## 🚀 Overview

This web application displays a **random inspirational programming quote** every time you refresh the page.  
Built with Go's efficient standard library, it combines simplicity, speed, and elegance.

---

## ✨ Features

- 🌍 **Random Quotes**: Refresh the page for a new programming quote.
- 🎨 **Clean Design**: A minimalist and modern user interface.
- ⚡ **Fast and Lightweight**: Powered by Go's blazing-fast standard library.
- 🧩 **Easily Extendable**: Add more quotes or features effortlessly.

---

## ⚙️ Local Installation

Follow these steps to set up and run the application locally:


1. **Clone the Repository**
    ```bash
   git clone https://github.com/Azaki-san/S25-core-course-labs.git
   cd S25-core-course-labs/app_golang

2. **Initialize Go Modules**
    ```base
    go mod init app_golang

3. **Run the Application**
    ```bash
    go run main.go
   
4. **Open in your browser**

   Navigate to http://localhost:8080 to view the application.


## 🖥️ Example Output

Here’s how the page will look:
    
    ----------------------------------------
    |        Programming Quote App         |
    |                                      |
    |   “The most frustrating thing        |
    |    about injuries is that they       |
    |   take so bloody long to heal”       |
    |              – Jason Statham         |
    |                                      |
    |      Refresh for a new quote!        |
    ----------------------------------------

---

## 🐳 Distroless Image Version

I implemented a **Distroless-based** image for the Golang application to improve security and reduce image size.

---

### 📏 Image Size Comparison

| Image Type       | Base Image Used                        | Approx. Size |
|------------------|---------------------------------------|-------------|
| **Standard Image** | `alpine:3.18`                        | **17MB**     |
| **Distroless Image** | `gcr.io/distroless/static:nonroot`  | **12MB**     |

The **Distroless image** is **5MB smaller** than the standard Alpine image.

---

### 📥 How to Build the Distroless Image

```bash
docker build -f distroless.Dockerfile -t azazaki/app_golang:distroless .
```

## 🛠️ Tech Stack

- **Language**: [Go (Golang)](https://golang.org)
- **Dependencies**: Uses only Go's standard library, including:
    - `net/http`: For handling HTTP requests.
    - `math/rand` and `time`: For generating random quotes with proper seeding.
    - `fmt`: For string formatting and output generation.

---

## 🧪 Unit Tests

Automated unit tests ensure the **Random Programming Quote Generator** functions correctly.

### ✅ How to Run Tests Locally
1. **Ensure Go is Installed**
   ```bash
   go version
   ```
2. **Navigate to the Application Directory**
   ```bash
   cd app_golang
   ```
3. **Run Unit Tests**
   ```bash
   go test -v ./...
   ```
    
### ✅ What’s Tested?
- **Server Status Code** → Ensures the `/` route returns a `200 OK` response.
- **Quote Retrieval** → Verifies that the response contains a valid quote.
- **Error Handling** → Ensures that invalid requests are handled gracefully.

These tests are executed **automatically** in the CI/CD pipeline on every push and pull request.

---

## 🔄 CI/CD Pipeline

The CI/CD pipeline automates testing, security scanning, and Docker deployment for the Random Programming Quote Generator.

### 🚀 What Happens on Every Push or PR?
1. **📦 Dependencies** → Ensures all required Go modules are installed.
2. **🔍 Linter** → Runs `golangci-lint` to enforce Go best practices.
3. **🧪 Unit Tests** → Runs `go test` to verify application functionality.
4. **🛡️ Security Scan** → Uses Snyk to detect vulnerabilities in dependencies.
5. **🐳 Docker Build & Push** → Builds and pushes a Docker image to Docker Hub.

## 🚀 Contributing

1. **Fork** this repository.
2. **Create** a new branch for your feature or fix.
3. **Commit** your changes and push to your branch.
4. **Create a Pull Request** to merge your changes into the `master` branch of this repository.

---

## 🛡️ License

This project is licensed under the **MIT License**. Feel free to use, modify, and distribute as needed.

---

## 💡 Ideas for Improvement

- API Integration: Fetch quotes from a public API for dynamic updates.
- Database Support: Store and manage quotes in a lightweight database like SQLite.
- Custom User Input: Allow users to submit their own quotes via a form.
- Styling Enhancements: Add animations or improved styles for a more engaging UI.
- REST API: Expose an API endpoint to retrieve quotes programmatically.

---

## ✨ Closing Note

The Random Programming Quote Generator is a simple yet fun application built to inspire developers. It combines Go's powerful standard library with creativity and scalability.
Feel free to explore, extend, and share your own version of this app!
