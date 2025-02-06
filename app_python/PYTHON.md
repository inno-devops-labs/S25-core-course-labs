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

<br>

## ⚙️ Unit Tests Implementation

**Setup**
- Pytest fixtures for clean client initialization 

**Validation**
- Strategic HTTP status and response checks

**Time**
- Precise timezone and sync verification

**Quality**
- Clear naming and documentation

**Coverage**
- Full API and core logic testing

This follows pytest best practices with minimal overhead while ensuring thorough validation.