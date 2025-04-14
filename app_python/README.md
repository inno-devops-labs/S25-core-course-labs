## Description
---

This is a simple Python web application built with `Flask` that displays the current local time in Moscow. It uses the `pytz` library for timezone management and provides a visually appealing, responsive frontend.

---

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.8 or higher
- Pip for managing Python packages

---


## Installation & Usage
---
1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd app_python
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    python main.py
    ```

4. Open the application in your browser:
    ```
    http://127.0.0.1:9200
    ```

---


## Docker usage
---
1. Build image
    ```bash
    docker build -t devopsapp .
    ```

2. Install dependencies:
    ```bash
    docker pull daniilzimin4/devopsapp:latest
    ```

3. Run:
    ```bash
    docker run -p 9200:9200 daniilzimin4/devopsapp:latest
    ```

4. Open in browser:
    ```
    http://127.0.0.1:9200
    ```

---