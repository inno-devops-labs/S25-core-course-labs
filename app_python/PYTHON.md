# Real-Time Moscow Clock 🕒

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Flask Version](https://img.shields.io/badge/flask-2.3.3-green)
![License](https://img.shields.io/badge/license-MIT-blue)


<!-- ![Alt text](image.png) -->

![Demo](time.gif)

### A simple real-time web application, which allows you to see Moscow time. App uses Flask framework and best practices in web development.

## ✨ Features
- **Real-time Updates**: Live clock updates every second
- **Accurate Timezone Handling**: Precise Moscow time using pytz
- **Responsive Design**: Interface which works on all devices

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (for version control)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/TimurZheksimbaev/S25-core-course-labs.git
   cd app_python
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   
   # Windows
   .\venv\Scripts\activate
   
   # Unix/MacOS
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   or 
   pip3 install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   flask run -h 0.0.0.0 -p 3000
   ```

5. **Open your browser and navigate to `http://localhost:3000`**

## 🧪 Testing

Code is covered in tests, including time accuracy and comparing current system time with time coming from web app

Run the test suite:
```bash
pytest
```

View test coverage:
```bash
pytest --cov=app tests/
```