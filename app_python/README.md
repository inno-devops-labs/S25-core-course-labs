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
## Building the Application

To access the application use docker-compose

```bash
docker-compose up --build
```

## Accessing the Application
- Backend: The backend service will be available at http://localhost:8080.
- Frontend: The frontend service will be available at http://localhost:3000.
- Grafana: The Grafana service will be available at http://localhost:3001.
## Endpoints
- GET /times: Fetch all time zones.
- GET /times/<name>: Fetch the current time for a given city.
- GET /visits: Fetch the number of visits.
## Unit tessts
To run the tests use :
```bash
python -m unittest discover -s tests
```

