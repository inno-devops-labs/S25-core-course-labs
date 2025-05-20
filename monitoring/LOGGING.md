# Logging Stack Documentation

## Overview
This document describes the logging stack setup using Grafana, Loki, and Promtail. The stack is designed to collect, aggregate, and visualize logs from our Python application.

## Components

### 1. Grafana
- **Purpose**: Web-based visualization and analytics platform
- **Port**: 3000
- **Features**:
  - Provides a user interface for querying and visualizing logs
  - Allows creation of dashboards and alerts
  - Integrates with Loki for log visualization
- **Access**: Available at http://localhost:3000

### 2. Loki
- **Purpose**: Log aggregation system
- **Port**: 3100
- **Features**:
  - Stores and indexes logs
  - Provides a query language (LogQL) for log analysis
  - Efficiently stores logs using object storage
- **Storage**: Uses a persistent volume for log storage

### 3. Promtail
- **Purpose**: Log collector
- **Port**: 9080
- **Features**:
  - Collects logs from various sources
  - Sends logs to Loki
  - Supports multiple log collection methods:
    - Docker container logs
    - System logs
    - Application-specific logs

## Configuration Details

### Docker Compose Setup
The `docker-compose.yml` file defines the following services:
- Grafana for visualization
- Loki for log aggregation
- Promtail for log collection
- Python application

### Promtail Configuration
The `promtail/config.yml` file configures log collection for:
- Docker container logs
- System logs
- Python application logs

## How to Use

1. Start the stack:
   ```bash
   cd monitoring
   docker-compose up -d
   ```

2. Access Grafana:
   - Open http://localhost:3000
   - Default credentials are disabled (anonymous access enabled)
   - Add Loki as a data source (URL: http://loki:3100)

3. View Logs:
   - In Grafana, go to Explore
   - Select Loki as the data source
   - Use LogQL to query logs
   - Example query: `{container="app_python"}`

## Log Collection
Logs are collected from:
- Docker containers (automatically)
- System logs (/var/log)
- Application-specific logs
  - Python app: /var/log/python_app/*.log

## Testing and Verification

### 1. Component Verification
- **Loki**: Verified using curl command `curl http://localhost:3100/ready`
  - Response: "ready" - indicating Loki is operational
- **Promtail**: Verified through Docker logs
  - Successfully collecting logs from containers
  - Properly configured with Docker socket access
- **Grafana**: Verified through web interface
  - Successfully connected to Loki
  - Able to query and display logs

### 2. Log Collection Testing
- **Python Application Logs**:
  - Verified collection of startup logs
  - Confirmed proper container name labeling
  - Tested with query: `{container="monitoring-app_python-1"}`
- **System Logs**:
  - Verified collection of system logs
  - Tested with query: `{job="varlogs"}`

### 3. Example LogQL Queries
- Basic container logs: `{container="monitoring-app_python-1"}`
- Error logs: `{container="monitoring-app_python-1"} |= "error"`
- Startup logs: `{container="monitoring-app_python-1"} |~ ".*startup.*"`
- System logs: `{job="varlogs"}`

## Screenshots

### 1. Grafana Explore View
![Grafana Logs View](screenshots/Screenshot%202025-05-18%20at%206.03.16%20PM.png)
*Grafana Explore showing Python application logs with Loki as data source*

### 2. Log Query Results
[Add screenshot of log query results in Grafana]

### 3. System Overview
[Add screenshot of the overall system showing all components working together]

## Troubleshooting
If logs are not appearing:
1. Check Promtail logs: `docker-compose logs promtail`
2. Verify Loki is running: `curl http://localhost:3100/ready`
3. Test Loki query: `curl -G -s "http://localhost:3100/loki/api/v1/query_range" --data-urlencode 'query={container="monitoring-app_python-1"}'`
4. Ensure Grafana data source is properly configured (URL: http://loki:3100) 