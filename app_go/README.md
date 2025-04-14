# Go Web Application: Guess the Number Game

## Overview
This is a simple web-based "Guess the Number" game built using the Gin framework. The server generates a random number between 1 and 100, and the user has to guess it. Feedback is provided on each guess.

## Features
- Generates a random number between 1 and 100.
- Provides feedback: "Too Low", "Too High", or "Correct".
- Resets the game after a correct guess.

## Installation

### Prerequisites
- Go 1.19 or later

### Steps
1. Clone the repository:
   ```bash
   git clone <your-repository-url>
   cd app_go

2. Install dependencies:
    ```bash
    go mod tidy

3. Run the application:
    ```bash
    go run main.go

4. Access at:
    http://localhost:8080