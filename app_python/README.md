# Python Moscow time application

## Overview

This web application returns Moscow time on the `/` page.

## Local installation and running

```bash
# Installing the repo itself
git clone https://github.com/m0t9/S25-core-course-labs -b lab1

# Setup virtual environment
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
cd S25-core-course-labs/app_python

# Running
uvicorn main:app --reload

# Testing
curl http://127.0.0.1:8000
```
