# Java Web Application - Omsk Timezone

## Overview
This project is a simple Java web application that displays the current time in Omsk. The application uses the Spark framework for creating the web server and Java's built-in **ZonedDateTime** and **ZoneId** classes for timezone management.
## Features
- Displays the current time in Omsk.
- Automatically updates the time upon refreshing the webpage.

## Technology Stack
- **Java:** Programming language used to develop the application.
- **Spark Framework:** Lightweight web framework for handling HTTP requests.

## Installation steps

Steps to configure the app locally:
1. **Clone the repository:**
   ```bash
       git clone https://github.com/DoryShibkova/S25-core-course-labs
   ```
2. **Navigate to the project directory:**
   ```bash
       cd app_Java
   ```
3. **Download the Spark framework:**
   - Visit Spark Framework and download the spark-core JAR file.
   - Place the JAR file in project directory.
     
4. **Compile the application:**
   ```bash
       javac -cp spark-core-2.9.3.jar web_app.java
   ```
5. **Run the application:**
   ```bash
       java -cp .:spark-core-2.9.3.jar web_app
   ```
6. **Open browser and go to:** http://localhost:4567/
