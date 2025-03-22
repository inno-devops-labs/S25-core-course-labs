# Logging Stack Setup

This document describes the logging stack setup using **Grafana Loki**, **Promtail**, and **Grafana**.

## Components

### 1. Loki
- **Role**: Log aggregation system.
- **Configuration**: Stores logs in a filesystem and provides an API for querying logs.
- **Port**: `3100`

### 2. Promtail
- **Role**: Log shipping agent.
- **Configuration**: Collects logs from the application and sends them to Loki.
- **Port**: `9080`

### 3. Grafana
- **Role**: Visualization tool.
- **Configuration**: Queries and displays logs stored in Loki.
- **Port**: `3000`

![alt text](screenshots\docker-compose.png)

## Setup

1. **Docker Compose**:
   - The `docker-compose.yml` file defines the services for the logging stack and the application.

2. **Configuration Files**:
   - `loki/config/loki-config.yaml`: Configures Loki.
   - `promtail/config/promtail-config.yaml`: Configures Promtail.

## Screenshots

### All Logs
![alt text](screenshots\app1.png)
![alt text](screenshots\app2.png)

### Python App Logs
![alt text](screenshots\py_app1.png)
![alt text](screenshots\py_app2.png)