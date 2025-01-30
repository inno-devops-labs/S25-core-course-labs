# Moscow Time Web Application

A simple Python web application built with **FastAPI** that displays the current time in **Moscow (MSK)**.

---

## Overview

This application serves an HTML page displaying the current time in **Moscow (MSK)**. It uses the `pytz` library to ensure accurate timezone handling and includes an image of Moscow for visual appeal.

---

## Features

- Displays the current time in **Moscow** in a bold, centered format.
- Includes an image of Moscow for visual appeal.
- Lightweight and minimalistic implementation.

---

## Local Installation

### Prerequisites

- Python 3.8 or higher installed.
- Install the required dependencies using `pip`.

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Nikoali01/S25-core-course-labs
   git checkout lab1
   cd app_python
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   uvicorn main:app --reload
   ```

4. **Access the Application**
    ```bash
    http://127.0.0.1:8000/time/moscow
    ```