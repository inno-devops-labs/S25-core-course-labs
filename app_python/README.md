# Flask Web App: Moscow Time

## Overview

This is a simple Python Flask web application that displays the **current time in Moscow**. The time updates every time the user refreshes the page, and is accurately timezone-adjusted using `pytz`.

---

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package manager)

(Optional but recommended):
- A virtual environment tool such as `venv`

---

## Installation

Clone the repository or download the project files and navigate to the project directory:

```bash
cd app_python
```

Create and activate a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

To start the Flask web server:

```bash
python app.py
```

Then open your browser and visit:

```
http://127.0.0.1:5000
```

Refresh the page to see the current time update in real-time.

---

## 🧪 Testing

I used **manual testing** and **code linting** to ensure quality:

### Manual Testing
How did I test it:
- Load the page and verify the current time is shown.
- Refresh the page to confirm the time updates.
- Confirm proper timezone formatting for Moscow.

### Code Quality Checks

Run these tools to check for linting and code quality:

```bash
flake8 app.py
python3 -m pylint app.py
```

---
