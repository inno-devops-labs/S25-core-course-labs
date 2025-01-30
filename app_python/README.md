# Moscow Time Web Application

A simple Flask-based web application that displays the current time in Moscow.

## Features
- Displays Moscow time in `HH:MM:SS` format
- Auto-refresh on page reload
- Unit tests with mocked time

## Installation

### 1. Clone the Repository
```bash
git clone --branch lab1 https://github.com/YehiaSobeh/S25-core-course-labs.git
cd S25-core-course-labs/app_python
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python src/app.py
```
Visit [http://localhost:5000](http://localhost:5000) in your browser.

### 5. Run Tests
```bash
python -m pytest tests/
```

## Project Structure
```
app_python/
├── app.py           # Main Flask application
├── tests/
│   ├── test_app.py      # Unit tests for the application
├── venv/                # Virtual environment (not included in Git)
├── .gitignore           # Git ignore file
├── requirements.txt     # Dependencies list
├── README.md            # Project documentation
├── PYTHON.md            # Python documentation
```

## Development
- Use `debug=True` in `app.py` for development mode (not recommended for production).
- Follow PEP8 standards.
- Update tests when modifying functionality.

