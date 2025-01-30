# Java Web Application: Random Hex Color Picker

## Overview

This project is a simple Java web application that generates a random hex color code using the **Spring Boot** framework. The application serves an HTML page displaying the randomly generated color with its corresponding hex code.

---
## Framework Choice: Spring Boot

### Why?
1. **Ease of Use**
   - Spring Boot simplifies the setup and development of new Spring applications with minimal configuration.
2. **Community Support**
   - A large community ensures robust support, extensive documentation, and numerous third-party integrations.
3. **Built-in Features**
   - Comes with built-in features like embedded servers, security, metrics, health checks, and externalized configuration.
4. **Thymeleaf Integration**
   - Thymeleaf provides a modern server-side Java template engine for web and standalone environments, making it ideal for rendering dynamic HTML content.
   
---
## Best Practices Applied
### 1. Dependency Injection
- Utilizes Spring's dependency injection to manage the lifecycle of beans, promoting loose coupling and better testability.
### 2. Component Scanning
- Ensures all components (controllers, services, etc.) are automatically detected and registered by specifying base packages in the main application class.
### 3. Code Organization
- Follows the **Single Responsibility Principle**:
  - The `RandomColorPickerImpl` class is responsible for generating random colors.
  - The `RandomHexController` handles HTTP requests and returns the view with the generated color.
### 4. Coding Standards
- Adheres to **Java naming conventions** and includes meaningful comments explaining key functionality.

---
## Implementation Details
### Endpoint: `/hex/color`
- **Purpose**: Generates and displays a random hex color code on an HTML page.
- **Logic**:
  - The `RandomColorPickerImpl` service generates a random RGB color and converts it to a hex string.
  - The `RandomHexController` retrieves the generated color and adds it as a model attribute.
### HTML Design
- The HTML page includes:
  - A heading displaying "Random Color Picker".
  - A div element styled with the generated color.
  - A paragraph displaying the hex code.
  - A button to regenerate the color by reloading the page.