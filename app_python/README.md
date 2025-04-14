# ⏰ Flask App: Moscow Time

### 📌 Overview
✔ This is a simple **Flask web application** that displays the **current time in Moscow** \
✔ The time updates dynamically

---

## 🚀 Features
✔ Displays **current Moscow time** using `pytz` \
✔ Lightweight **Flask-based** server \
✔ Unit tests \
✔ Styled with **HTML and CSS** \
✔ Good code style

---

## 🐳 Run via Docker image from Docker Hub
```sh
docker pull petrel312/flask_app:latest
docker run -p 5000:5000 petrel312/flask_app:latest
```

---

## 🛠 Local Installation and Run
```sh
git clone https://github.com/Petrel321/S25-core-course-labs.git
cd S25-core-course-labs
python3 -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt
cd app_python
python web.py
```

---

## 🛠 Local Installation and Build the Docker Image

```sh
git clone https://github.com/Petrel321/S25-core-course-labs.git
cd S25-core-course-labs/app_python
docker build -t any_docker_image_name .
```
