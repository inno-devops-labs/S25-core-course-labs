# Time Zone Application

This project is a full-stack application that allows users to view the current time for different cities. The backend is built with Flask and SQLAlchemy, and the frontend is built with React. The application uses PostgreSQL as the database.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Docker](#docker)
- [Environment Variables](#environment-variables)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Node.js](https://nodejs.org/) (for frontend development)
- [Python](https://www.python.org/downloads/) (for backend development)

## Installation

1. **Clone the repository**:

```bash
git clone https://github.com/your-username/time-zone-app.git
cd time-zone-app
```
2. **Install dependencies**:
Frontend:
```bash
cd frontend
yarn install
```
Backend:
```bash
cd backend
pip install -r requirements.txt
```
3. **Usage**
Start three-layer architecture of app:
```bash
docker-compose up -d db
```