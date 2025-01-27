# Random Number Generator Web Application

## Overview

This is a web application that displays a random number (between 0 and 100) each time the page is refreshed. The web application is built using Go and the standard library's `net/http` package for handling web requests. 

## Installation Guide

### Prerequisites

Before you begin, ensure you have the following installed:

*   **Go 1.16+**

### Steps

1.  **Clone the Repository:**

    Clone the project repository to your local machine and navigate to the project directory:

    ```bash
    git clone <repo_url>
    cd <project_directory>
    ```

2. **Navigate to app_golang Folder:**

   Change your current directory to the application folder:
    ```bash
   cd app_golang
    ```

3.  **Run the Application:**

    Execute the following command to start the application:

    ```bash
    go run main.go
    ```

    This command will compile and run the application from the `main.go` file.

### Troubleshooting

If you encounter an error, please ensure that port 8000 is available. You can either make this port available or modify the port number in the `main.go` file to another available port.
