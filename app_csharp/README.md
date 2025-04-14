# Moscow Time Web Application (C#)

![.NET](https://img.shields.io/badge/.NET-8.0-blue)  
![ASP.NET Core](https://img.shields.io/badge/Framework-ASP.NET_Core-green)

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
