# Moscow Time Web Application

Web application that returns current Moscow time in JSON format.

## Features

- Returns JSON response with timezone and current time in human-readable and machine-readable ISO format
- Auto-updating current time on each request
- PEP8 compliant code with `Black` formatter
- Lightweight local installation

## Installation

### Prerequisites

- Python 3.9+
- `pip` package manager

### Local Setup

1. Clone the repository:

```bash
git clone https://github.com/nikitashlyahktin/S25-core-course-labs
cd S25-core-course-labs/app_python
```

1. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Start the development server:

```bash
python3 app.py
```

1. Access the API endpoint with a web browser: `http://localhost:5000`

## Example Response

```json
{
  "current_time": "2025-01-26 13:53:55",
  "timezone": "Europe/Moscow"
}
```

## Project Structure

```txt
app_python/
├── app.py            # Main web application code
├── requirements.txt  # Dependency list
├── PYTHON.md         # Technical documentation
└── README.md         # User documentation
```

## Documentation

See [PYTHON.md](PYTHON.md) for technical implementation details.
