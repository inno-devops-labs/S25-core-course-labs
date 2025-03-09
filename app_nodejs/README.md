# Node.js Web Application

![Node CI](https://github.com/Sedoxxx/S25-core-course-labs/actions/workflows/node_ci.yml/badge.svg)

## Overview
This is a simple Node.js + Express application that displays the current time in Moscow (MSK). When you access the homepage, it will show you the current date and time in a well-formatted string with trcking the number of visits to the endpoint.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install Dependencies**:
   Ensure you have [Node.js](https://nodejs.org/) installed on your machine. Then, run the following command to install the required dependencies:
   ```bash
   npm install
   ```

---
## Running the Application

1. **Start the Server**:
   To start the application, run the following command:
   ```bash
   npm start
   ```
   This will start the server on port `3000` by default (or the port specified in the `PORT` environment variable).

2. **Access the Application**:
   Open your browser and navigate to:
   ```
   http://localhost:3000
   ```
   You should see the current time in Moscow displayed on the page.

---
## Environment Variables

If you want to run the application on a different port, you can set the `PORT` environment variable before starting the server. For example:
```bash
PORT=4000 npm start
```
This will start the server on port `4000`.

---

## Development

1. **Install Nodemon (Optional)**:
   For development, you can use `nodemon` to automatically restart the server whenever you make changes to the code. Install it globally or as a development dependency:
   ```bash
   npm install -g nodemon
   ```
   or
   ```bash
   npm install --save-dev nodemon
   ```

2. **Run with Nodemon**:
   If you have `nodemon` installed, you can start the server in development mode using:
   ```bash
   nodemon app.js
   ```
---

### API endpoints
      
   - `GET /`: Returns the current time in Moscow
   - `GET /metrics`: Returns Prometheus metrics
   - `GET /visits`: Returns the number of times the time endpoint has been accessed
   
## Testing

To test the application, simply visit the homepage (`http://localhost:3000`) and verify that the current time in Moscow is displayed correctly.

## Unit Tests

The application includes automated unit tests written with Mocha, Chai, and Supertest. These tests verify that the web application functions as expected and include:

- **Response Status and Content Type Check:**  
  Ensures that the homepage returns a 200 status code and the correct content type (HTML).

- **Response Content Validation:**  
  Verifies that the homepage contains the expected welcome message and that the time is formatted in the `YYYY-MM-DD HH:MM:SS MSK` format.

- **Time Accuracy Check:**  
  Compares the displayed time with the system time (using the Moscow timezone) to ensure that any discrepancy is within a two-second threshold.

### Running the Unit Tests

To run the unit tests, execute the following command in your terminal:
```bash
npm test


---
