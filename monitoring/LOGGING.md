# LOGGING

**Loki**, **Promtail**, and **Grafana**. The stack is designed to provide a centralized solution for log management in a Dockerized environment.

---

## Overview

The logging stack is built to provide a centralized solution for log management in a Dockerized environment. It includes the following components:

1. **Loki**: Log aggregation and storage.
2. **Promtail**: Log forwarding and labeling.
3. **Grafana**: Log visualization and querying.

Each component plays a specific role in ensuring that logs are collected, stored, and accessible for analysis.

---

## Components

### 1. **Loki**

- **Role:** Loki is responsible for ingesting, storing, and querying logs. It acts as the central log storage system.
- **Key Features:**
  - Lightweight and efficient log aggregation.
  - Supports multi-tenancy and label-based querying.
  - Provides an API for log ingestion and querying.
- **How It Works:**
  - Promtail sends logs to Loki via its push API (`http://loki:3100/api/prom/push`).
  - Loki stores logs with associated metadata (labels) and makes them queryable through Grafana or its API.

---

### 2. **Promtail**

- **Role:** Promtail acts as a log forwarder, collecting logs from various sources and forwarding them to Loki.
- **Key Features:**
  - Reads logs from specified paths (e.g., Docker container logs).
  - Adds labels to logs for better categorization and filtering.
  - Supports dynamic log discovery.
- **How It Works:**
  - Promtail monitors log files (e.g., `/var/lib/docker/containers/*/*log`) and forwards them to Loki.
  - It applies labels (e.g., `job=docker`) to logs for easier querying.

---

### 3. **Grafana**

- **Role:** Grafana serves as the visualization and querying interface for logs stored in Loki.
- **Key Features:**
  - Provides a web-based UI for exploring and analyzing logs.
  - Supports advanced log queries using Loki's query language.
  - Allows users to create dashboards and alerts based on log data.
- **How It Works:**
  - Grafana connects to Loki as a data source.
  - Users can query logs using expressions like `{job="docker"}` in the Explore tab.
  - Logs are displayed in a user-friendly format, making it easy to debug and monitor applications.

---

## Workflow

1. **Log Generation:**
   - Applications running in containers generate logs, which are stored in Docker's log files (`/var/lib/docker/containers/*/*log`).

2. **Log Collection:**
   - Promtail reads these log files, adds relevant labels, and forwards them to Loki.

3. **Log Storage:**
   - Loki ingests the logs and stores them with their associated metadata (labels).

4. **Log Visualization:**
   - Users access Grafana at `http://localhost:3000` and use the Explore tab to query logs from Loki, enabling real-time monitoring and debugging.

---

## Testing the Stack

To ensure the stack is functioning correctly:

1. Start the services using `docker-compose up -d`.
2. Generate logs by interacting with the Python or C# applications (`http://localhost:8081` or `http://localhost:8082`).
3. Access Grafana at `http://localhost:3000` and use the Explore tab to query logs (e.g., `{job="docker"}`).
4. Verify that logs appear in Grafana and match the expected labels.

---

## Resulting logs

### All of the docker logs

![all-the-logs](./assets/all_logs.png)

### Python App Logs

**Container logs:**

```bash
PS E:\Documents\Innop\C3\S2\devops\S25-core-course-labs\monitoring> docker logs monitoring-python_app-1
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:5000 (Press CTRL+C to quit)
INFO:     172.19.0.1:46952 - "GET / HTTP/1.1" 200 OK
INFO:     172.19.0.1:46952 - "GET /favicon.ico HTTP/1.1" 404 Not Found
INFO:     172.19.0.1:35310 - "GET / HTTP/1.1" 200 OK
INFO:     172.19.0.1:35310 - "GET /favicon.ico HTTP/1.1" 404 Not Found
```

**Grafana logs:**

![grafana-py-logs](./assets/logs_py.png)

### C# App Logs (BONUS)

**Container logs:**

```bash
PS E:\Documents\Innop\C3\S2\devops\S25-core-course-labs\monitoring> docker logs monitoring-cs_app-1
warn: Microsoft.AspNetCore.DataProtection.Repositories.EphemeralXmlRepository[50]
      Using an in-memory repository. Keys will not be persisted to storage.
warn: Microsoft.AspNetCore.DataProtection.KeyManagement.XmlKeyManager[59]
      Neither user profile nor HKLM registry available. Using an ephemeral key repository. Protected data will be unavailable when application exits.
warn: Microsoft.AspNetCore.DataProtection.KeyManagement.XmlKeyManager[35]
      No XML encryptor configured. Key {8f2e0364-ac40-4936-8322-fe564a855d7e} may be persisted to storage in unencrypted form.
warn: Microsoft.AspNetCore.Hosting.Diagnostics[15]
      Overriding HTTP_PORTS '8080' and HTTPS_PORTS ''. Binding to values defined by URLS instead 'http://+:80'.
info: Microsoft.Hosting.Lifetime[14]
      Now listening on: http://[::]:80
info: Microsoft.Hosting.Lifetime[0]
      Application started. Press Ctrl+C to shut down.
info: Microsoft.Hosting.Lifetime[0]
      Hosting environment: Production
info: Microsoft.Hosting.Lifetime[0]
      Content root path: /app
warn: Microsoft.AspNetCore.HttpsPolicy.HttpsRedirectionMiddleware[3]
      Failed to determine the https port for redirect.
```

**Grafana logs:**

![grafana-cs-logs](./assets/logs_cs.png)
