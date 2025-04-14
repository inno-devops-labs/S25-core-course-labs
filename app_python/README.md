# Python Moscow Time Web App

## Overview

This application displays the current time in Moscow.
Refresh the page to see the displayed time update.

## Requirements

- Python 3.8+
- See requirements.txt for Python dependencies

## Installation

- Clone repo:

```git clone https://github.com/G3nD4/S25-core-course-labs.git```

- Go to root app folder:

```cd app_python```

- Install requirements:

```pip install -r requirements.txt```

## Usage

- Run app:

```python app.py```

- Run tests:

```pytest```

## Build Docker Image

- You can build and run Docker Image locally using following commands:

```docker build -t python-web:latest .```

```docker run -d --name python-web -p 5000:5000 python-web:latest```

- Or you can pull my image and run it:

```docker pull g3nd4/python-web:latest```

```docker run -d --name python-web -p 5000:5000 g3nd4/python-web:latest```
