# Metrics Collection with Prometheus

This document outlines the setup and configuration of Prometheus for collecting metrics from our applications and services.

## Prometheus Setup

### 1. Integration with Docker Compose

The `docker-compose.yml` file has been updated to include Prometheus, which is now integrated with our existing monitoring stack. The Prometheus service is configured to:

- Run the official Prometheus image (v2.45.0)
- Expose port 9090
- Mount the `prometheus.yml` configuration file
- Connect to the logging network

### 2. Prometheus Configuration

The `prometheus.yml` file configures Prometheus to scrape metrics from:

- Prometheus itself (for self-monitoring)
- Loki (logging service)
- Python Flask application (main application)

### 3. Prometheus Targets

After starting the services, Prometheus targets are accessible at http://localhost:9090/targets. 

**Note:** Screenshots of the Prometheus targets and Grafana dashboards can be found in the `screenshots/` directory.

## Dashboard and Configuration Enhancements

### 1. Grafana Dashboards

Grafana dashboards have been set up for both Loki and Prometheus:

- Screenshots are available in the `screenshots/` directory:
  - `prometheus_dashboard.png`: The Python App Metrics dashboard using Prometheus as a data source
  - `loki_dashboard.png`: The logs dashboard using Loki as a data source
  - `grafana_dashboards.png`: Overview of all available dashboards

### 2. Service Configuration Updates

All services in the `docker-compose.yml` file have been updated with:

#### Memory Limits
- Loki: 512MB
- Prometheus: 512MB
- Promtail: 256MB
- Grafana: 256MB
- Python App: 256MB

#### Log Rotation
All services have been configured with log rotation using the json-file driver:
- Max file size: 10MB
- Max number of files: 3

### 3. Metrics Gathering

The Python Flask application (main app) has been enhanced to expose Prometheus metrics:

- Added the `prometheus-client` package to `requirements.txt`
- Created new endpoints to expose metrics at `/metrics`
- Defined several metrics:
  - `page_views_total`: Counter for page views with page label
  - `health_checks_total`: Counter for health checks
  - `http_request_duration_seconds`: Histogram for HTTP request duration

## How to Use

1. Start all services using: `docker-compose up -d`
2. Access Prometheus UI at: http://localhost:9090
3. Access Grafana at: http://localhost:3000
4. View Prometheus targets at: http://localhost:9090/targets
5. View metrics from the Python app at: http://localhost:5001/metrics

## Screenshots

![Screenshot 1](screenshots/Screenshot%202025-03-23%20at%2013.49.09.png)

![Screenshot 2](screenshots/Screenshot%202025-03-23%20at%2013.51.25.png)

![Screenshot 3](screenshots/Screenshot%202025-03-23%20at%2013.52.51.png)

![Screenshot 4](screenshots/Screenshot%202025-03-23%20at%2015.43.34.png)

## Conclusion

The integration of Prometheus with our existing monitoring stack provides comprehensive visibility into the performance and behavior of our main Python application. With Grafana dashboards, we can visualize both logs (via Loki) and metrics (via Prometheus) in a unified interface. 