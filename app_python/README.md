# Python Web Application: Moscow Time

## Introduction

This is a simple web application built with Python and Flask to display the current time in Moscow. The time updates whenever the page is refreshed.

### Instructions

1. Clone this repository:

```bash
https://github.com/dprostiruk/S25-core-course-labs.git
```

2. Navigate to the `app_python` folder:

```bash
cd app_python
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python app.py
```

5. Open a browser and visit:

`http://127.0.0.1:5000/`

> *Note*: Ensure your system's timezone settings are correct to display the accurate Moscow time.

## Docker commands
### Build the Docker Image

```bash
docker build -t shelma13/devops-lab2 .
```

### Run the container locally

```bash
docker run -p 5000:5000 shelma13/devops-lab2
```

### Push Image to Docker Hub

```bash
docker tag shelma13/devops-lab2 shelma13/devops-lab2:latest
docker push shelma13/devops-lab2:latest
```

### Pull and Run from Docker Hub

```bash
docker pull shelma13/devops-lab2:latest
docker run -p 5000:5000 shelma13/devops-lab2:latest
```

### Requirements

- Python 3
- Flask
- pytz

### Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [Flask Framework](https://flask.palletsprojects.com/)
- [Timezones in Python](https://docs.python.org/3/library/datetime.html#time-zones)
