### README.MD

# Random Hex Color Picker Web Application
A simple Java web application built with **Spring Boot** that generates and displays a random hex color code.
---
## Overview
This application serves an HTML page displaying a randomly generated color along with its corresponding hex code. It uses Spring Boot for backend processing and Thymeleaf for rendering the dynamic HTML content.
---
## Features
- Displays a randomly generated color in a centered box.
- Shows the hex code of the generated color below the color box.
- Provides a button to regenerate the color by reloading the page.
- Lightweight and easy-to-understand implementation.
---
## Local Installation
### Prerequisites
- Java Development Kit (JDK) 17 or higher installed.
- Apache Maven installed.
### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/Nikoali01/S25-core-course-labs
   git checkout lab1
   cd app_java
2. **Build the Project**
   ```bash
   mvn clean install
3. **Run the Application**
   ```bash
   mvn spring-boot:run
4. **Access the Application**
    ```bash
    http://localhost:8080/hex/color