# Moscow Time Web Application

This is a Python web application built with FastAPI that displays the current time in Moscow.

## Application setup

1. Clone the repo
```
git clone https://github.com/tolmachdr/S25-core-course-labs -b lab1
```
2. Setup virtual environment
```aiignore
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```
3. Go to the folder and run the app
```aiignore
cd app_python
uvicorn main:app --reload
```

## Docker 

To run this application you also can use docker, for this you need to:

1. Build image
```
docker build -t python-app .
```

2. Run the container
```aiignore
docker run -p 8000:8000 python-app
```

OR

1. Pull existing image from dockerhub
```aiignore
docker pull dtolmach/python-app:latest
```
2. Run the container
```aiignore
docker run -p 8000:8000 python-app
```



