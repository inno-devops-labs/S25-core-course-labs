# Python Web Application

## Description
 A Python web application that displays the current time in Moscow.

## Prerequisites
- Python 3.x
- pip

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Angelika2707/S25-core-course-labs.git
cd app_python
```
    
### 2. Set up a Virtual Environment

Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows

```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install the Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

Linux
```bash
python3 main.py
```
Windows
```bash
python main.py
```

Then you can find the application on the address: `http://127.0.0.1:5000`

# Docker

### How to build?
```bash
docker build -t lab2 .
```

### How to pull?
```bash
docker pull angelika2707/lab2
```

### How to run?
```bash
docker run -p 5000:5000 angelika2707/lab2
```