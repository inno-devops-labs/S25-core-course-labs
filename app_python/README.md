# Moscow Time Web Application

This is a Python web application built with **FastAPI** that displays the current time in Moscow. The application is designed to follow best practices described in this [repo](https://github.com/zhanymkanov/fastapi-best-practices). Read about it in `PYTHON.md`.

---

## Project Structure

```
moscow_time_app/
├── src/
│   └── main.py              # FastAPI application code
├── tests/
│   └── test_main.py         # Unit tests for the application
├── .gitignore               # List of files that ignores by git
├── PYTHON.md                # Justification for my salary as a Python developer :-)
├── README.md                # Project documentation
└── requirements.txt         # Project dependencies
```

---


## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/KonstantinPetrovichQWERTY/IU-DevOps-S25.git
   cd moscow_time_app
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment**:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Running the Application

To start the FastAPI application, run the following command:

```bash
uvicorn src.main:app --reload
```

- The `--reload` flag enables auto-reloading, so the server restarts whenever you make changes to the code.
- Open your browser and navigate to `http://127.0.0.1:8000/get_moscow_time`. You should see the current time in Moscow displayed in JSON format.
- To see the SwaggerUI documentation navigate to `http://127.0.0.1:8000/docs`.

---

## Testing the Application

To run the unit tests, use the following command:

```bash
pytest
```

### Test Cases

1. **Test Endpoint Response**:
   - Verifies that the `/get_moscow_time` endpoint returns a valid response (contain `'moscow_time'` key) with a status code of `200`.

2. **Test Time Format**:
   - Ensures that the returned time is in the correct `YYYY-MM-DD HH:MM:SS` format.

3. **Test Time Updates**:
   - Confirms that the displayed time updates between requests.

---

## Dependencies

All dependencies you can find in `requirements.txt`.

---
