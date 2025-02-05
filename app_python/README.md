# Python Web Application: Moscow Time

This Python web application displays the current time in Moscow. It uses the Flask framework and follows best practices for coding and testing.

## Features

- Displays the current time in Moscow.
- Refresh the page to see updated time.
- Clean and responsive UI with minimal styling.

## Getting Started

### Prerequisites

1. Python 3.7 or later installed.
2. Install dependencies from `requirements.txt`.

### Installation

1. Clone this repository:

   ```bash
   git clone <repository-url>
   cd app_python
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. Run the Flask app:

   ```bash
   python main.py
   ```

2. Open a browser and visit `http://127.0.0.1:5000/`.

## Docker

### How to build?

   ```bash
   cd app_python
   docker build -t <app-name> .
   ```

### How to pull?

   ```bash
   docker pull yoqubdavlatov/app_python:latest
   ```

### How to run?

   ```bash
   docker run -p 5000:5000 yoqubdavlatov/app_python:latest
   ```

## Development

- Follow PEP 8 coding standards.
- Use `pytz` for timezone-specific handling.

## Testing

### Runtime testing

- Verify the time updates on refresh manually.

### Unit tests

- To run unit tests run:

```bash
   pytest 
   ```
