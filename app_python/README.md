# 

## Description
A simple Django application that displays the current time in Moscow.

## Installation
```bash
git clone https://github.com/Galyusha/S25-core-course-labs.git
git checkout lab1
cd app_python
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python3 manage.py runserver

```
## Docker
### **Build the Image**
```sh
docker build -t my-django-app .
```
### **Run the Container**
```sh
docker run -p 8000:8000 my-django-app
```
### **Pull from Docker Hub**
```sh
docker pull g1l1a/my-django-app
docker run -p 8000:8000 g1l1a/my-django-app
```
## Distroless Image Version

**Distroless Image**: A minimal version of the app that uses distroless images, resulting in a smaller image size and a reduced attack surface.
To build the distroless image:
```bash
docker build -f distroless.Dockerfile -t my-django-app-distroless .
```
