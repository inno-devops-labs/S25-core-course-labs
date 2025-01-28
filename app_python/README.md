# Moscow Time Web Application

A Python web application built with **FastAPI** to display the current time in Moscow.

---

## **Features**
- Displays the current time in Moscow (UTC+3) in a visually appealing interface.
- Automatically updates the time on page refresh.
- Responsive design for seamless viewing on all devices.

---

## **Technologies Used**
- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python.
- **Jinja2**: Templating engine for rendering HTML pages.
- **Uvicorn**: ASGI server for running FastAPI applications.

---

## **Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/secretanry/S25-core-course-labs.git
   cd app_python
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Run the application:
   ```bash
   uvicorn main:app --reload
5. Open your browser and navigate to:
   ```text
   http://localhost:8000

## **Project Structure**
```
app_python/
├── main.py                # FastAPI application
├── requirements.txt       # Dependencies
├── templates/             # HTML templates
│   └── index.html
├── README.md              # Project documentation
├── PYTHON.md              # Best practices and coding standards
└── .gitignore             # Files to ignore in version control
```


## **Dependencies**
1. fastapi
2. uvicorn
3. jinja2
4. pytz

### **License**
This project is licensed under the **MIT License**.