
---

# Python Web Application

![Python CI](https://github.com/Sedoxxx/S25-core-course-labs/actions/workflows/python_ci.yml/badge.svg)


## Overview
This Flask-based Python web application displays the current time in Moscow (MSK). When you access the homepage, it will show you the current date and time in a well-formatted string with trcking the number of visits to the endpoint.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<your-username>/<your-repo>.git
   cd <repository-folder>
   ```

2. **Create a Virtual Environment**:
   To isolate dependencies, create a virtual environment:
   ```bash
   python3 -m venv env
   ```

3. **Activate the Virtual Environment**:
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```
   - On Windows:
     ```bash
     .\env\Scripts\activate
     ```

4. **Install Dependencies**:
   Install the required dependencies using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

---

## Running the Application

1. **Start the Server**:
   To start the application, run the following command:
   ```bash
   python main.py
   ```
   This will start the server on port `5000` by default.

2. **Access the Application**:
   Open your browser and navigate to:
   ```
   http://localhost:5000
   ```
   You should see the current time in Moscow displayed on the page.

---

## Environment Variables

If you want to run the application on a different port, you can set the `FLASK_RUN_PORT` environment variable before starting the server. For example:
```bash
export FLASK_RUN_PORT=4000
python main.py
```
This will start the server on port `4000`.

---

## Development

1. **Enable Debug Mode (Optional)**:
   For development, you can enable Flask's debug mode to automatically reload the server when changes are made. Set the `FLASK_ENV` environment variable:
   ```bash
   export FLASK_ENV=development
   python main.py
   ```

---

### API endpoints
      
   - `GET /`: Returns the current time in Moscow
   - `GET /metrics`: Returns Prometheus metrics
   - `GET /visits`: Returns the number of times the time endpoint has been accessed

## Testing

To test the application manually, visit the homepage (`http://localhost:5000`) and verify that the current time in Moscow is displayed correctly.

---

## Unit Tests

The application includes automated unit tests written with `pytest`. These tests ensure that the web application functions as expected and include:

- **Response Status and Content Type Check:**  
  Ensures the homepage returns a 200 status code and the correct `text/html; charset=utf-8` content type.
  
- **Response Content Validation:**  
  Verifies that the homepage contains the expected welcome message and that the time is formatted correctly with the 'MSK' timezone abbreviation.
  
- **Time Accuracy Check:**  
  Compares the displayed time with the system time (both using the Moscow timezone) to ensure that any discrepancy is within a two-second threshold.

### Running the Unit Tests

To run all the unit tests, execute the following command in your terminal:
```bash
python -m pytest
```
This command will run the entire test suite and display a summary of the test results. Ensure that all tests pass to confirm that the application is functioning correctly.

