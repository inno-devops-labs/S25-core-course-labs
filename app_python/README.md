# Instructrions to run the project

## Requirements:

- Python 3.9
- Flask
- pytz

## To run the web application on your machine, follow the steps:

1. Clone the repository:

```bash
    git clone https://github.com/mngcndl/S25-core-course-labs
    cd S25-core-course-labs/app_python
```

2. Create virtual environment:

```bash
    python -m venv venv
    source venv/bin/activate # for MacOS and Linux
    venv\Scripts\activate # for Windows
```

3. Install dependencies locally using the command:

```bash
    pip install -r requirements.txt
```

4. Run the application:

```bash
    python app.py
```

5. Go to your web browser and open the url http://127.0.0.1:5000

## To run the web application on your machine using Docker, follow the steps:

If you already have all the files locally, build the image:

```bash
    docker build -t mangocandle/app_python:latest .
```

OR

1. Pull the image:

```bash
    docker pull mangocandle/app_python:latest .
```

2. Run the image:

```bash
    docker run -p 5000:5000 mangocandle/app_python:latest
```
