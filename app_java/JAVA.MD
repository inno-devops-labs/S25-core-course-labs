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

---

## Unit Tests

Unit tests are crucial for ensuring the correctness and reliability of the application. Below is a description of the unit tests created for this project:

1. **Test for Correct Format (`testPickRandomColor_Format`)**:
   - **Purpose**: Ensures that the generated hex color string adheres to the correct format (`#RRGGBB`).
   - **Assertions**:
     - The returned color string is not null.
     - The string starts with `#`.
     - The string has exactly 7 characters.
     - The string matches the regular expression `^#[0-9A-Fa-f]{6}$`.

2. **Test for RGB Range Validation (`testPickRandomColor_RangeValidation`)**:
   - **Purpose**: Verifies that each RGB component (red, green, blue) is within the valid range `[0, 255]`.
   - **Assertions**:
     - Each component (R, G, B) is parsed from the hex string and validated to ensure it falls within the range `[0, 255]`.

3. **Test with Mocked Random Object (`testPickRandomColor_MockedRandom`)**:
   - **Purpose**: Tests the behavior of the `pickRandomColor` method when a mocked `Random` object is used, ensuring predictable results.
   - **Assertions**:
     - The returned color string is not null.
     - The string matches the expected value (`#808080`) based on the mocked `Random` object.

These tests ensure that the core functionality of the `RandomColorPickerImpl` class is robust and behaves as expected under various scenarios.

---

## Best Practices Applied in Testing

1. **Test Coverage**:
   - The tests cover all critical aspects of the `RandomColorPickerImpl` class, including format validation, range checks, and behavior with mocked dependencies.

2. **Mocking Dependencies**:
   - A mocked `Random` object is used to test deterministic behavior, ensuring consistent results during testing.

3. **Assertion Clarity**:
   - Clear and specific assertions are used to validate the output, making it easy to identify issues if a test fails.

4. **Integration with CI Workflow**:
   - The tests are integrated into the CI workflow, ensuring they are executed automatically on every push or pull request.
