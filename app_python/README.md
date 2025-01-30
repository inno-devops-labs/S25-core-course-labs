# Moscow Time Display Application (FastAPI)

## Overview

This application is built using FastAPI and provides the current time in Moscow. It is lightweight and fast.

## Prerequisites

Ensure you have Python installed on your system. This application requires Python 3.7 or later.

## Installation

1. Clone the repository :

   ```sh
   git clone https://github.com/KaramKhaddour/S25-core-course-labs.git
   cd S25-CORE-CORSE-LABS/app_python
   ```

2. Install the required dependencies:

   ```sh
   pip install -r requirements.txt
   ```

## Running the Application

To start the FastAPI server, run the following command:

```sh
uvicorn main:app --reload
```

This will start the development server and enable automatic reloading for changes in the source code.

## Accessing the API

Once the application is running, you can access it via:

- **API Endpoint:** `http://127.0.0.1:8000` (or another specified host/port)
- **Interactive API Documentation:**
  - Swagger UI: `http://127.0.0.1:8000/docs`
