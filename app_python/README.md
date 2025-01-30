# ⏰ Moscow Time Web Application (Python)

## 📌 Overview
This is a simple Flask-based web application that displays the current time in Moscow.

## 🚀 Installation and Running

### 🤡 *Clone the Repository*

```bash
git clone <url>
cd app_python
```

###  *Create a Virtual Environment and Install Dependencies*

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 🏃 *Run*

```bash
python app.py
```

### 🐳 *Run via Docker image from Dockerhub*
```bash
docker pull enot0704/moscow-time-app:v1.0
docker run -d -p 5000:5000 enot0704/moscow-time-app:v1.0
```
### 🐳 *Local Build Image and Run*
```bash
git clone https://github.com/Andrew-dev-cmd/S25-core-course-labs.git
cd S25-core-course-labs/app_python
docker build -t name .
docker run -d -p 5000:5000 name
```

### 📖 *Open in your Browser*

`http://127.0.0.1:5000/`

## ☁️ Running Tests

### *Run Unit Tests*

```bash
python -m unittest discover tests_python
```

### *Run Integration Tests*

```bash
python tests_python/integration_test.py
```

## 📱 Technologies

- **Python 3.x**
- **Flask**
- **pytest & unittest** (for testing)