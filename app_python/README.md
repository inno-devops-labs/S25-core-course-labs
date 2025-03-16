Here’s the updated `README.md` file with the changes we made to the application:

---

# Moscow Time Web Application

## Overview
This is a simple web application that displays the current time in Moscow. The application is built using the Flask framework.

## Features
- Displays the current time in Moscow.
- Tracks the number of times the application is accessed.
- Saves the visit count in a `visits.txt` file for persistence.
- Provides a `/visits` endpoint to display the total number of visits.
- Updates the time and visit count upon page refresh.

---

## Local Installation

### Prerequisites
- Python 3.7+
- Flask
- pytz

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/Muhhhibullo/S25-core-course-labs.git
   cd S25-core-course-labs.git/app_python
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Run the application:
   ```sh
   python3 app.py
   ```

---

## Docker

### Clone and Build the Docker Image
1. Clone the repository:
   ```sh
   git clone https://github.com/Muhhhibullo/S25-core-course-labs.git
   cd S25-core-course-labs.git/app_python
   ```

2. Build the Docker image:
   ```sh
   docker build -t lab2 .
   ```

3. Run the Docker container:
   ```sh
   docker run -p 5000:5000 -v $(pwd)/data:/data lab2
   ```

### Pull and Run the Docker Image from Docker Hub
1. Pull the Docker image:
   ```sh
   docker pull deedjei/lab2
   ```

2. Run the Docker container:
   ```sh
   docker run -p 5000:5000 -v $(pwd)/data:/data deedjei/lab2
   ```

---

## Unit Tests
Test suite ensures:
- Successful application startup.
- Correct timezone handling.
- Proper time formatting.
- Template rendering accuracy.
- Persistence of visit count in the `visits.txt` file.

Run tests with:
```bash
pytest test_app.py
```

---

## Changes Made
1. **Added Counter Logic**:
   - The application now tracks the number of times it is accessed.
   - The visit count is saved in a `visits.txt` file for persistence.

2. **New `/visits` Endpoint**:
   - Added a new endpoint to display the total number of visits.

3. **Persistence with Docker Volumes**:
   - Updated the `docker-compose.yml` file to include a volume for the `visits.txt` file.
   - Ensured the `/data` directory is created if it doesn’t exist.

4. **Resolved FileNotFoundError**:
   - Added a function to create the `/data` directory if it doesn’t exist.

5. **Fixed Port Conflicts**:
   - Resolved port 5000 conflicts by stopping conflicting processes or using a different port.

6. **Documentation Updates**:
   - Updated the `README.md` file to reflect the new features and changes.
   - Created a `12.md` file to document the results of commands and steps taken.

---

## Usage
1. Access the home page:
   - Open your browser and go to `http://localhost:5000`.
   - The page will display the current time in Moscow and the number of visits.

2. Access the `/visits` endpoint:
   - Go to `http://localhost:5000/visits` to see the total number of visits.

3. Verify persistence:
   - Stop and restart the application.
   - The visit count should persist across restarts.

---

