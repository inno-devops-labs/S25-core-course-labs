# Python Web Application

## Overview
This Python web application displays the current time in Moscow using Flask.

## Local Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/emiliogain/S25-core-course-labs.git
   cd S25-core-course-labs
   git checkout lab1
   cd app_python
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the application:
   ```sh
   python main.py
   ```
4. Open `http://127.0.0.1:5000/` in your browser.

## 🐳 Running with Docker

### How to Build?
```sh
cd app_python
docker build -t  my-python-app .
```

### How to Pull?
```sh
docker pull emiliogain/my-python-app:latest
```

How to Run?
```sh
docker run -p 8080:5000 emiliogain/my-python-app
```

## Unit Tests

This project includes unit tests to verify the correctness and reliability of the application.

### **Running Unit Tests**
Run the following command to execute the tests:
```sh
pytest
```

### **What is Tested?**  

- **Status Code**: Homepage (`/`) returns **200 OK**.  
- **Template Rendering**: `index.html` loads correctly.  
- **Time Presence**: `current_time` exists in the template.  
- **Time Format**: Time follows **HH:MM:SS** format.  
- **Moscow Time**: Displays the correct time for **Europe/Moscow**.  
