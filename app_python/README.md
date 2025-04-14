# Python Web Application

## Overview

This is a simple Python web application that displays the current time in the Moscow timezone.

**Stack**: `Python 3.x`, `Flask`, `pytz`

## Prerequisites

Make sure you have Python 3.x is installed on your machine. You can check by running:
```bash
python3 --version
```
or
```bash
python --version
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/WellNotWell/DevOps-labs.git
cd app_python
```
    
### 2. Set up a Virtual Environment

**On macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**

```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install the Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python3 app.py
```
or
```bash
python app.py
```

### 5. Access the application 
Access the application in your web browser at `http://127.0.0.1:5000/`.

## Docker

### How to Build the Docker Image

```bash
cd app_python
docker build -t lab2 .
```

### How to Pull the Docker Image
```bash
docker pull wellnotwell/lab2
```

### How to Run the Docker Image
```bash
docker run -p 5000:5000 wellnotwell/lab2
```
