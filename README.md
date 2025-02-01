# My Python Web Application

## Introduction

This is a Python web application that uses PostgreSQL as its database and a frontend built with a modern JavaScript framework.

## Setup

### Prerequisites

- Python 3.9
- PostgreSQL 13
- Node.js 20
- Yarn

### Installation

**Clone the repository**:

   ```bash
   git clone https://github.com/JulyMartynova/S25-core-course-labs/blob/lab1/app_python
   cd your_repo
   ```
Set up the backend:

``` bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Set up the frontend:

``` bash
cd ../frontend
yarn install
```
Set up the database:

``` bash
cd ../database
psql -h localhost -U myuser -d times -f init.sql
```
Running the Application
Start the backend:

``` bash
cd backend
source venv/bin/activate
python main.py
```
Start the frontend:

``` bash
cd ../frontend
yarn start
```
## Accessing the Application
The backend will be running on http://localhost:8080.
The frontend will be running on http://localhost:3000
