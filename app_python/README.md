# Overview

A simple Python web application displaying the current time in **Moscow**.

🌍 **Live Moscow Time**  

---

## Features

✔️ Displays **current Moscow time** in a stylish UI  
✔️ Uses **Flask** for lightweight backend handling  
✔️ Supports **MSK Timezone (UTC+3)**  

## Technologies Used

- **Python** (3.8+)
- **Flask** (Web framework)
- **pytz** (Timezone handling)

## Installation Guide

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/bakinasa/S25-devops-engineering-labs.git
cd app_python
```

### 2️⃣ Create a Virtual Environment

```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3️⃣ Install Dependencies

```sh
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```sh
python app.py
```

Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

### Docker

Build and run the Docker image:

```sh
docker build -t moscow-time-app .
docker run -p 5000:5000 -d moscow-time-app
```

Get the latest image from Docker Hub:

```sh
docker pull bakinasa/moscow-time-app:latest
docker run -p 5000:5000 -d bakinasa/moscow-time-app:latest
```
