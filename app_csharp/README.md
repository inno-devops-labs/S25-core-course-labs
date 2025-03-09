# Moscow Time Web Application (C#)

![.NET](https://img.shields.io/badge/.NET-8.0-blue)  
![ASP.NET Core](https://img.shields.io/badge/Framework-ASP.NET_Core-green)
![CI/CD Workflow](https://github.com/yeaphm/S25-core-course-labs/actions/workflows/csharp_app_ci.yml/badge.svg)

## Overview  

A web application that displays the current time in **Moscow (MSK)** using ASP.NET Core.  

---

## Features  

- Real-time Moscow time (UTC+3) using `DateTime` calculations.  
- MVC architecture for clean separation of concerns.  

---

## Prerequisites  

- **.NET 8 SDK** or later.  
  - Download: [https://dotnet.microsoft.com/download](https://dotnet.microsoft.com/download)  
  - Verify installation:  

    ```bash
    dotnet --version  # Should return "8.x.x" or higher
    ```

---

## Local Installation  

1. **Clone the repository**:  

   ```bash
   git clone https://github.com/yeaphm/S25-core-course-labs.git
   cd app_csharp/MoscowTimeApp
   ```

2. **Restore dependencies**:  

   ```bash
   dotnet restore
   ```

3. **Run the application**:  

   ```bash
   dotnet run
   ```

4. **Access the app**:  
   Open `http://localhost:5101` in your browser.  

---

## Dependencies  

- ASP.NET Core Runtime (managed via `.csproj` file).  

See [CSHARP.md](CSHARP.md) for technical details.  

## Docker Instructions

[Dockerhub](https://hub.docker.com/r/efimpuzhalov/moscow-time-csharp-app)

### Build the Image

```bash
docker build -t dockerhub-username/moscow-time-csharp-app:latest .
```

### Run the Container

```bash
docker run -p 8080:80 dockerhub-username/moscow-time-csharp-app:latest

# you can use mine:
docker run -p 8080:80 efimpuzhalov/moscow-time-csharp-app:latest
```

### Push to Docker Hub

```bash
docker push dockerhub-username/moscow-time-csharp-app:latest
```

### Key Features  

- 🐳 Multi-stage build for optimized image size.  
- 🛡️ Runs as non-root user (`appuser`).  
- 🔒 Excludes unnecessary files via `.dockerignore`.  

## Distroless Image Version

[Dockerhub](https://hub.docker.com/r/efimpuzhalov/moscow-time-csharp-app-distroless)

### Usage

```bash
docker build -f distroless.Dockerfile -t moscow-time-distroless .
docker run -p 8080:80 moscow-time-distroless

# you can use mine:
docker run -p 8080:80 efimpuzhalov/moscow-time-csharp-app-distroless:latest
```

### Distroless Features

- 🔐 **Nonroot Execution**: Runs as nonroot by default ([official documentation](https://github.com/dotnet/dotnet-docker/blob/main/documentation/distroless.md))
- 🐋 **Ultra-Small**: for regular .NET images
- 🛡️ **Hardened Security**: No shells or package managers

## Unit Tests

Unit tests are implemented to ensure the correctness and reliability of the application's functionality. They validate that the `HomeController` returns the accurate current time in Moscow (UTC+3).

### Running Tests

To execute the unit tests, follow these steps:

1. **Ensure Dependencies Are Installed**:

   ```bash
   dotnet restore
   ```

2. **Run the Tests**:

   ```bash
   dotnet test
   ```

### Test Details

- **Framework** : xUnit
- **Test Project** : MoscowTimeApp.Tests
- **Description** :
  - Tests the `Index` action in `HomeController` to verify the returned Moscow time.
  - Mocks `ILogger<HomeController>` to isolate the test scope.
  - Asserts that the `ViewBag.MoscowTime` value matches the expected Moscow time.
- **Assertions** :
  - Ensures `ViewBag.MoscowTime` contains a valid timestamp in `yyyy-MM-dd HH:mm:ss` format.
  - Confirms the displayed time is within an expected tolerance of execution delay.

## **CI Pipeline Overview**

This repository includes a **GitHub Actions CI** pipeline to ensure code quality, security, and automated deployment for the C# application.

### **🔄 CI Workflow Triggers**

The workflow runs on **pull requests** affecting:
- The `app_csharp/` directory
- The `.github/workflows/csharp_app_ci.yml` file

### **🛠️ CI Workflow Steps**

#### **1️⃣ Build, Lint, and Test**
- Sets up .NET 8.0.x environment
- Caches NuGet packages for faster builds
- Runs `dotnet format` for code style enforcement
- Executes `dotnet build` and `dotnet test` with Release configuration

#### **2️⃣ Security Check**
- Scans solution file with **Snyk** for vulnerabilities
- Requires `SNYK_TOKEN` secret for authenticated scanning

#### **3️⃣ Docker Build & Push**
- Builds and pushes **two optimized images**:
  - **Standard .NET image** (`latest` tag)
  - **Distroless image** (`distroless` tag)
- Publishes to Docker Hub under `${{ secrets.DOCKER_USERNAME }}`
- Uses GitHub Actions cache for build optimization