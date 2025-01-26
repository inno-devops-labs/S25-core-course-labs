# Swift Web Application for Displaying Current Moscow Time

## Overview

This is a simple web application developed using the **Vapor** framework in Swift. The application displays the current time in Moscow and updates the displayed time every time the page is refreshed. It uses the **SwiftDate** library to handle time zone and regional time, converting the current time into the Moscow time zone.

## Features

- Displays the current Moscow time in the format `yyyy-MM-dd HH:mm:ss`.
- Dynamically updates the time upon page refresh.
- Built using **Vapor** and **SwiftDate** libraries.

## Steps to Install and Run

### Prerequisites

Ensure you have the following installed on your machine:

- **Xcode** (latest version recommended)
- **Homebrew** (for package management)
- **Vapor**: If you don't have Vapor installed, follow the instructions at [Vapor Installation](https://docs.vapor.codes) to install it.

### Steps to Install and Run

1. Clone the repository to your local machine:

   ```bash
   git clone <repository_url>
   cd app_swift
      ```

2. Install the dependencies using Vapor:

   ```bash
   vapor update
   ```
   
3. Build and run the project:
   
   ```bash
   vapor run serve
   ```

4. Open a browser and visit <http://localhost:8080> to see the current Moscow time.

## Project Structure

- **Sources/App/routes.swift:** Contains the route definition that fetches the Moscow time and renders it using the Leaf template engine.
- **Resources/Views/index.leaf:** The HTML template that displays the current Moscow time.
- **Package.swift:** The Swift Package Manager file that manages the project's dependencies.

## Dependencies

- Vapor: A web framework for Swift.
- SwiftDate: A library for handling date and time with ease in Swift.

## Requirements

- Swift 5.4+
- macOS 10.15+ (or equivalent Linux setup for Vapor deployment)
- Xcode (for local development)
