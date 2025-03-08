# Python Application Documentation

## Overview

This is a simple FastAPI application that provides the current time in Moscow timezone.

## Requirements

- Python 3.8+
- Dependencies listed in requirements.txt

## Setup

1. Create a virtual environment:

```bash
python -m venv .venv
```

2. Activate the virtual environment:

```bash
source .venv/bin/activate  # On Unix/macOS
.venv\Scripts\activate     # On Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the application

```bash
python app.py
```

The application will be available at <http://127.0.0.1:8000>

## Unit tests

The application includes comprehensive unit tests implemented using pytest. The tests cover:

1. **Endpoint availability test (`test_read_main`)**:
   - Verifies that the endpoint responds with a 200 status code
   - Checks if the response contains the expected "current_time" field

2. **Time format test (`test_time_format`)**:
   - Validates that the returned time string follows the correct format (YYYY-MM-DD HH:MM:SS)
   - Ensures the time string can be properly parsed

3. **Timezone test (`test_timezone`)**:
   - Confirms that the returned time is in Moscow timezone
   - Compares the returned hour with the actual Moscow time

### Running tests

To run the tests, execute:

```bash
pytest
```

For test coverage report:

```bash
pytest --cov=app
```

## Best practices applied

- Used pytest as the testing framework for its rich features and wide community support
- Implemented TestClient from FastAPI for endpoint testing
- Added comprehensive assertions to verify both response structure and data validity
- Included timezone-specific tests to ensure correct time conversion
- Used fixtures and proper test isolation
- Implemented coverage reporting to track test completeness
