# Logging Stack Documentation

This document provides an overview of the logging stack implemented for this project, detailing each component's role and how they work together to provide a centralized logging solution.

## Overview

The logging stack consists of three main components:

1. **Loki** - A horizontally-scalable, highly-available log aggregation system
2. **Promtail** - An agent that ships the contents of local logs to Loki
3. **Grafana** - A visualization and analytics platform that can query and display data from Loki

Together, these components create a complete logging solution that collects, stores, and allows visualization of logs from various sources.

## Components

### Loki

Loki is a log aggregation system inspired by Prometheus, designed to be cost-effective and easy to operate. It indexes and groups log streams using labels, similar to how Prometheus manages metrics.

**Key Features:**
- Designed to be cost-effective with log storage separated from indexing
- Uses the same label system as Prometheus to organize log streams
- Can ingest logs from many popular agents including Promtail
- Provides a powerful query language (LogQL) for log exploration

**Configuration:**
Our Loki configuration is stored in `monitoring/loki-config.yaml` and is set up to:
- Run without authentication for development purposes
- Store data temporarily in local storage
- Accept HTTP connections on port 3100

### Promtail

Promtail is an agent that discovers log files, attaches labels to them, and ships them to Loki.

**Key Features:**
- Automatically discovers log files and assigns labels
- Tails files (follows their contents as they grow)
- Efficiently ships logs to Loki
- Can scrape logs from various sources, including files and Docker containers

**Configuration:**
Our Promtail configuration is in `monitoring/promtail-config.yaml` and is set up to:
- Discover and collect system logs
- Collect Docker container logs
- Specifically target NGINX logs from our demo application
- Collect Python Flask application logs
- Send all logs to the Loki instance

### Grafana

Grafana is an open-source platform for monitoring and observability that allows you to query, visualize, and alert on metrics and logs from various data sources.

**Key Features:**
- Supports various data sources, including Loki
- Provides a rich UI for creating dashboards
- Offers powerful visualization options
- Supports alerting based on thresholds

**Configuration:**
- Grafana is provisioned with an automatic Loki data source connection
- Sample dashboards are provided to visualize all application logs
- Anonymous access is enabled with admin privileges for development purposes

## How It Works

1. **Log Collection**:
   - Promtail discovers log files on the host system
   - It attaches labels to these logs based on their source
   - For Docker containers, it recognizes container logs and labels them accordingly
   - For the Python app, it collects logs from the dedicated volume

2. **Log Aggregation**:
   - Logs are sent to Loki, which indexes them by their labels
   - Loki efficiently stores and compresses the log content
   - Labels are used for quick filtering and searching

3. **Visualization**:
   - Grafana connects to Loki as a data source
   - Users can create queries using LogQL to filter and display logs
   - Dashboards provide a visual interface for log exploration

## Python Application Integration

The logging stack has been extended to support our Python Flask application:

### App Modifications

The Python Flask application has been configured to:
- Write logs to `/home/appuser/logs/app.log`
- Log at INFO level with timestamps and log levels
- Log various events including page access, errors, and health checks
- Output logs to both file and stdout

### Docker Setup

The integration uses:
- A shared volume (`python-app-logs`) between the Python app and Promtail
- Container networking to enable service discovery
- Proper dependency ordering so Loki and Promtail are available before the app starts

### Monitoring

Custom dashboards are provided for:
- Viewing all Python app logs
- Filtering for error logs
- Analyzing access patterns

## Querying Logs

Loki uses LogQL, a query language inspired by PromQL, but adapted for logs. Some example queries:

- **Python app logs**: `{job="python_app"}` - Shows all logs from the Python application
- **Python errors only**: `{job="python_app"} |= "ERROR"` - Shows only error logs from the Python app

## Setting Up and Running

The entire stack is configured to run with Docker Compose:

```bash
cd monitoring
docker-compose up -d
```

After running, you can access:
- Grafana at http://localhost:3000
- Loki API at http://localhost:3100
- Python Flask app at http://localhost:5001
- Demo NGINX app at http://localhost:8080

## Screenshots

![Screenshot 1](screenshots/Screenshot%202025-02-27%20at%2022.57.59.png)

![Screenshot 2](screenshots/Screenshot%202025-02-27%20at%2022.58.13.png)

![Screenshot 3](screenshots/Screenshot%202025-02-27%20at%2022.59.21.png)

![Screenshot 4](screenshots/Screenshot%202025-02-27%20at%2022.59.37.png)