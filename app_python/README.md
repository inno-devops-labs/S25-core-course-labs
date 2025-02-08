# 📌 Moscow Time Web Application 🕒

## 🌍 Overview
This is a **Flask-based web application** that displays the **current time in Moscow**.  
The time **automatically updates every second** to ensure real-time accuracy.

## 📦 Features
✅ Displays real-time **Moscow time (MSK)**  
✅ **Auto-refresh** every second using JavaScript  
✅ Uses **Flask framework** for a lightweight and efficient backend  
✅ **Well-structured code** following best practices  
✅ Includes **unit tests** to ensure reliability  

## 🚀 Local Installation
Follow these steps to run the application on your local machine:

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/anasalatasiuni/S25-core-course-labs.git
cd app_python
```
### 2️⃣ Install Dependencies
Ensure you have python3 installed, then run:
```bash
pip install -r requirements.txt
```
### 3️⃣ Run the Application
```bash
python app.py
```

Visit: http://127.0.0.1:5000/ in your browser.

## 🛠 Requirements
- Python 3.x
- Flask
- pytz (for time zone handling)


## 📦 Running with Docker

This section explains how to build, pull, and run the application using Docker.
### 🔨 How to Build the Docker Image?
If you want to build the image locally, run:
```bash
docker build -t moscow-time-app .
```
This will create a Docker image named moscow-time-app.
### 🔽 How to Pull from Docker Hub?
The image is available on Docker Hub, you can pull it directly using:
```bash
docker pull anasalatasi/moscow-time-app:latest
```
### 🚀 How to Run the Container?
Once the image is built or pulled, start the container by running:
```bash
docker run -p 5000:5000 moscow-time-app
```
Then visit: http://localhost:5000
