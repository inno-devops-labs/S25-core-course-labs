# Node.js Web Application

## Overview
This is a simple Node.js + Express application that displays the current time in Moscow (MSK). When you access the homepage, it will show you the current date and time in a well-formatted string .

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
## Testing

To test the application, simply visit the homepage (`http://localhost:3000`) and verify that the current time in Moscow is displayed correctly.

---
