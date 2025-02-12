# Moscow Time Web Application

## Overview

This is a web app that shows current date and time in Moscow. It is written in Python with Bottle framework.

## Requirements

* Python 3.12

## Installation

Clone this repository:

```bash
git clone https://github.com/cuprum-acid/devops-labs.git -b lab1
```

Open directory:

```bash
cd devops-labs/app_python
```

Install virtual environment and dependencies:

```bash
python -m venv venv
```

```bash
source venv/bin/activate # Linux/Mac
```

```bash
venv\Scripts\activate # Windows
```

```bash
pip install -r requirements.txt
```

Run the app:

```bash
python app.py
```

Now it is available on `localhost:8080` in browser. Or you can run in terminal:

```bash
curl localhost:8080
```

## Run tests

If you want to run automatic tests, then you need to install additional packages:

```bash
pip install pytest==8.3.4
```

```bash
pip install requests==2.32.3
```

They were not included in `requirements.txt` because they are not required to run application

After that run:

```bash
pytest test_app.py
```
