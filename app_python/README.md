# Python Web Application

## Overview

This project is a time-tracking web application that displays the current Moscow time and provides real-time updates to
the user. The application is built using Flask.

## Features

- Real-time clock update using JavaScript and Flask.
- Clean and user-friendly interface.
- Easy deployment using requirements.txt.

## Prerequisites

Make sure you have Python 3.x and libraries from requirements.txt installed on your system.

## Docker

### How to build?
```
podman build -t app_python .
```

### How to pull?
```
podman pull docker.io/kartofanych/app_python:latest
```
   
### How to run?
```
podman run -p 8080:8080 app_python
```