# Python App [![CI](https://github.com/MohamadSafi/S25-core-course-labs/actions/workflows/ci.yaml/badge.svg)](https://github.com/MohamadSafi/S25-core-course-labs/actions/workflows/ci.yaml)

## **Overview**

A simple Python web application built with **Flask** that:

- Displays the **current time in Moscow (MSK)**.
- Tracks and **persists the number of visits** using a **persistent counter** stored in a `visits` file.
- Exposes an **endpoint `/visits`** to display the visit count.

## **Features**

✅ **Real-Time MSK Time**: Shows the current time in Moscow.

✅ **Visit Counter**: Tracks the number of times the application is accessed.

✅ **Persistence**: The visit count **remains unchanged** even if the container is restarted.

✅ **Lightweight & Simple**: Only requires Flask and `pytz` to run.

✅ **Containerized with Docker**: Easily deployable anywhere.

---

## **Installation**

1. **Clone the repository**:

   ```bash
   git clone https://github.com/MohamadSafi/S25-core-course-labs.git
   cd S25-core-course-labs

   ```

2. **Create and activate a virtual environment** (recommended):

   ```bash
   python -m venv env
   source env/bin/activate  # Linux/Mac
   # or
   env\Scripts\activate  # Windows
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask application**:

   ```bash
   python main.py

   ```

5. **Access the application** in your browser:
   - [**http://127.0.0.1:5050**](http://127.0.0.1:5050/) → Shows the **current time in Moscow**.
   - **http://127.0.0.1:5050/visits** → Displays the **visit count**.

---

## **Docker Support**

The application is containerized with **Docker** for easy deployment.

### **Build the Docker Image**

```bash
docker build -t billyboone/python-moscow-time:latest .
```

### **Run the Docker Container with Persistence**

To ensure the **visit count persists**, **mount a volume**:

```bash
docker run --rm -p 5050:5050 -v $(pwd)/data:/app/data billyboone/python-moscow-time:latest

```

📌 **This will store the visit count in `./data/visits` on your local machine.**

📌 The number of visits **remains the same** even after container restarts.

### **Push the Docker Image to Docker Hub**

To upload your built image:

```bash
docker login
docker tag billyboone/python-moscow-time:latest billyboone/python-moscow-time:v1
docker push billyboone/python-moscow-time:v1
```

### **Pull and Run from Docker Hub**

To pull and run the image from Docker Hub:

```bash
docker pull billyboone/python-moscow-time:latest
docker run --rm -p 5050:5050 -v $(pwd)/data:/app/data billyboone/python-moscow-time:latest
```

---

## **CI/CD Workflow**

We use **GitHub Actions** to automate testing, linting, and Docker builds.

### **Workflow Steps**

1. **Dependencies Installation**: Installs required Python packages.
2. **Linter Check**: Runs `flake8` to check for code style issues.
3. **Unit Tests**: Executes `pytest` to ensure correctness.
4. **Docker Login**: Authenticates to Docker Hub using GitHub Secrets.
5. **Docker Build & Push**: Builds and pushes the Docker image if tests pass.

---

## **New Endpoint Details**

| **Endpoint** | **Description**               | **Example Response**                            |
| ------------ | ----------------------------- | ----------------------------------------------- |
| `/`          | Shows **current Moscow time** | `"Current time in Moscow: 2025-06-10 12:45:00"` |
| `/visits`    | Displays **number of visits** | `"Total Visits: 10"`                            |

---

## **Persistence Verification**

To **verify that visits persist**, follow these steps:

1. **Run the container**:

   ```bash
   docker run -d -p 5050:5050 -v $(pwd)/data:/app/data --name python_app billyboone/python-moscow-time:latest
   ```

2. **Visit the app multiple times**:
   - Open **http://localhost:5050**
   - Check visit count at **http://localhost:5050/visits**
3. **Stop & Restart the container**:

   ```bash
   docker stop python_app
   docker start python_app
   ```

4. **Check visit count again** (it should persist!).

---

### **Cleanup**

To remove all Docker containers and images:

```bash

docker stop python_app
docker rm python_app
docker rmi billyboone/python-moscow-time:latest
```
