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
