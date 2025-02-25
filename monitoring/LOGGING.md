# Logging

## Logging Stack Overview

This logging stack consists of **Loki**, **Promtail**, and **Grafana** to provide centralized logging and monitoring for our applications (**app_python** and **app_js**).

### Components:

1. **Loki** - A log aggregation system that stores and indexes logs.
2. **Promtail** - A log collector that ships logs to Loki.
3. **Grafana** - A visualization tool that queries logs from Loki.
4. **Applications** - `app_python` and `app_js` generate logs that are collected by Promtail.

---

## Docker Compose Setup

The `docker-compose.yml` file defines all services and ensures they are networked together. 

### **Loki**
- Listens on port `3100`.
- Stores logs in `loki-data` volume.

### **Promtail**
- Monitors container logs (`/var/lib/docker/containers`).
- Uses `promtail.yml` for configuration.
- Sends logs to Loki (`http://loki:3100`).

### **Grafana**
- Runs on port `3000`.
- `datasources.yml` configures Loki as a data source.
- Provides a UI for querying logs.

### **Application Logs**
- `app_python` (Flask) runs on port `5000`.
- `app_js` (Express) runs on port `3001`.
- Both applications log their outputs, which are collected by Promtail.

---

## Promtail Configuration

The `promtail.yml` file configures Promtail to:
- Scrape logs from `app_python` and `app_js` containers.
- Tag logs with appropriate labels (container name, log source).
- Forward logs to Loki.


---

## Testing the Logging Stack

1. Start the logging stack using:
   ```sh
   docker-compose up -d
   ```
2. Open Grafana at `http://localhost:3000`.
3. Add **Loki** as a data source (if not pre-configured).
4. Go to **Explore** and select **Loki**, then run a query:
   ```logql
   {service_name="app_python"}
   ```
5. Logs from `app_python` should appear in the dashboard. And with other applications the order is the same.

---

## Screenshots

### System Overview
![System Overview](images/Screenshot%20from%202025-02-23%2008-05-28.png)
### System Logs
![System Logs](images/Screenshot%20from%202025-02-23%2009-06-21.png)
### app_python
![app_python](images/Screenshot%20from%202025-02-23%2009-24-27.png)
### app_js
![app_js](images/Screenshot%20from%202025-02-23%2009-24-53.png)
### Grafana
![Grafana](images/Screenshot%20from%202025-02-23%2009-56-08.png)

