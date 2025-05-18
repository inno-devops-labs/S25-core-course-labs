# Monitoring Setup Documentation

## Overview
This document describes the monitoring setup for our application using Prometheus, Grafana, and Loki.

## Components

### Prometheus
- **Port**: 9090
- **Purpose**: Metrics collection and storage
- **Configuration**: 
  - Scrapes metrics every 15 seconds
  - Collects metrics from:
    - Prometheus itself
    - Loki
    - Grafana
    - Python application
- **Memory Limit**: 512MB
- **Health Check**: Available at `http://localhost:9090/-/healthy`

### Grafana
- **Port**: 3000
- **Purpose**: Metrics visualization
- **Configuration**:
  - Anonymous access enabled
  - Admin role for anonymous users
- **Memory Limit**: 512MB
- **Health Check**: Available at `http://localhost:3000/api/health`
- **Dashboards**:
  - Loki Dashboard (ID: 13407)
  - Prometheus Dashboard (ID: 3662)

### Loki
- **Port**: 3100
- **Purpose**: Log aggregation
- **Memory Limit**: 256MB
- **Health Check**: Available at `http://localhost:3100/ready`

### Promtail
- **Purpose**: Log collection
- **Memory Limit**: 128MB
- **Health Check**: Available at `http://localhost:9080/ready`

### Python Application
- **Port**: 5001 (mapped to 8000)
- **Memory Limit**: 256MB
- **Health Check**: Available at `http://localhost:8000/health`

## Verification Steps

1. Access Prometheus targets at `http://localhost:9090/targets` to verify all services are being scraped
2. Access Grafana at `http://localhost:3000` to view dashboards
3. Check service health through Docker:
   ```bash
   docker-compose ps
   ```

## Screenshots

### Prometheus Targets
![Prometheus Targets](screenshots/targets.png)
*All services are successfully scraped by Prometheus*

### Prometheus Dashboard
![Prometheus Dashboard](screenshots/prometheus.png)
*Prometheus metrics visualization in Grafana*

### Loki Dashboard
![Loki Dashboard](screenshots/loki.png)
*Log visualization using Loki in Grafana*

## Log Rotation
Log rotation is handled by Docker's built-in logging driver with the following configuration:
- Maximum file size: 10MB
- Maximum number of files: 3
- Compression enabled

## Memory Limits
All services have been configured with appropriate memory limits to prevent resource exhaustion:
- Grafana: 512MB
- Prometheus: 512MB
- Loki: 256MB
- Promtail: 128MB
- Python App: 256MB 