# METRICS

## Overview

This document details the setup and configuration of Prometheus for monitoring applications and services. It includes integration steps, configuration files, and validation screenshots.

---

## Prometheus Setup

### 1. About Prometheus

Prometheus is an open-source monitoring system that collects and stores metrics as time series data. It scrapes metrics from configured endpoints and allows querying via PromQL.

### 2. Integration with Docker Compose

The existing `docker-compose.yml` was extended to include Prometheus.

### 3. Prometheus Configuration

Prometheus is configured to collect metrics from Loki and other services.

There are targets from `http://localhost:9090/targets`:

![Targets](images/Screenshot%20from%202025-02-23%2012-17-35.png)

## Dashboards

### Loki

![Loki](images/Screenshot%20from%202025-02-23%2011-53-19.png)
![Loki](images/Screenshot%20from%202025-02-23%2012-00-22.png)

### Prometheus

![Loki](images/Screenshot%20from%202025-02-23%2012-01-26.png)
![Loki](images/Screenshot%20from%202025-02-23%2012-01-44.png)

## Service configuration
### Memory limit
```yaml
deploy:
  resources:
    limits:
      memory: 512M
```
### Health check
```yaml
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost:3100/health"]
  interval: 30s
  timeout: 10s
  retries: 3
```

### Log rotation
```yaml
logging:
  driver: "json-file"
  options:
    max-size: "100m"
    max-file: "3"
```
