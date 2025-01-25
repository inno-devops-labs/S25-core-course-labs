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