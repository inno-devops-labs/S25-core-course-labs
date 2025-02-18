# Metrics

## Service Configuration Updates

### Log Rotation
- All services are configured to use JSON file logging with log rotation.
- Log files are limited to a size of `10MB`.
- A maximum of `3` rotated log files are retained for each service.

### Memory Limits
- A memory limit of `512MB` is set for all containers.

## Screenshots

### Prometheus Targets

![Prometheus Targets](screenshots/targets.png)

### Loki Dashboard

![Grafana Loki Dashboard](screenshots/loki_dashboard.png)

### Prometheus Dashboard

![Grafana Prometheus Dashboard](screenshots/prometheus_dashboard.png)
