# Python Sample Application

## Overview

This is a simple python web application that shows current time in Moscow.

## Copy sources

- Clone this repository and navigate to the project directory:

```bash
git clone https://github.com/raleksan/S25-core-course-labs -b lab1
cd S25-core-course-labs/app_python
```

## Installation

- _Optional:_ activate nix-shell environment for Nix-based systems

```bash
nix-shell -p python312 python312Packages.pip
```

- Install virtual environment and dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

- Run the application:

```bash
python3 app.py
```

- Application usage: open <http://127.0.0.1:5000> or

```bash
curl 127.0.0.1:5000
```

## Docker

- Build Docker container

```bash
docker build --tag raleksan/app_python:v0.1 .
```

> Note: Do not forget to replace nickname `raleksan` into your own.

- Login into Dockerhub for image pull

```bash
docker login
```

- Push image into Dockerhub

```bash
docker push raleksan/app_python:v0.1
```

- Pull image from Dockerhub

```bash
docker pull raleksan/app_python:v0.1
```

- Run image

```bash
docker run -p 8080:8080 raleksan/app_python:v0.1
```
