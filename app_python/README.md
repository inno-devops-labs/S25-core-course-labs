Here’s the updated `README.md` file with the Python Flask application instructions added, following the same structure and style as the Node.js application:

---

# Python Web Application

## Overview
This Flask-based Python web application displays the current time in Moscow (MSK). When you access the homepage, it will show you the current date and time in a well-formatted string.

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

## Testing

To test the application, simply visit the homepage (`http://localhost:5000`) and verify that the current time in Moscow is displayed correctly.

---


