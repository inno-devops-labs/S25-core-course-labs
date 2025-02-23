# Monitoring Setup Documentation

## Prometheus Setup

### Components Overview

- Prometheus: Metrics collection and storage
- Loki: Log aggregation
- Grafana: Visualization platform

### Configuration Details

1. Prometheus is configured to scrape metrics from:

   - Itself (localhost:9090)
   - Loki (3100)
   - Python application (8000)
   - Rust application (8080)

2. Memory Limits:

   - Prometheus: 512MB
   - Loki: 512MB
   - Grafana: 512MB
   - Python Web App: 256MB
   - Rust Web App: 256MB
   - Promtail: 256MB

3. Log Rotation:
   - Max file size: 10MB
   - Max number of files: 3
   - Using json-file logging driver
   - Custom tags for Python and Rust apps

### Grafana Dashboards

1. Loki Dashboard:

   - Using template ID 13407
   - Configured for log visualization
   - [Screenshot of Loki dashboard]

2. Prometheus Dashboard:
   - Using template ID 3662
   - Configured for metrics visualization
   - [Screenshot of Prometheus dashboard]

### Verification Steps

1. Access Prometheus targets at `http://localhost:9090/targets`
2. Access Grafana at `http://localhost:3000`
   - Username: admin
   - Password: admin

[Include screenshots of Prometheus targets page and Grafana dashboards here]
