# Service Configuration Updates

It has been added the following : log rotation mechanisms, memory limits, Grafana dashboards, and metrics gathering.

## Log Rotation Mechanisms

To prevent log files from consuming excessive disk space, a log rotation mechanism has been implemented for all services using the `json-file` logging driver. The following options have been applied:

- `max-size`: Limits the size of each log file to 10MB.
- `max-file`: Retains up to 3 rotated log files.

Services affected:
- Loki
- Promtail
- Grafana
- Prometheus
- Python App
- Go App

## Memory Limits and Reservations

Memory limits and reservations have been specified for all services to ensure optimal resource allocation and prevent memory overuse. The following values have been set:

- **Loki, Promtail, Grafana, Prometheus**:
  - Memory Limit: 512MB
  - Memory Reservation: 256MB

- **Python App**:
  - Memory Limit: 200MB
  - Memory Reservation: 80MB

- **Go App**:
  - Memory Limit: 150MB
  - Memory Reservation: 60MB

These configurations help maintain system stability and performance by limiting resource consumption.

## Grafana Dashboards

Two dashboards have been set up in Grafana to visualize logs and metrics:

1. **Loki Dashboard**:
   - Imported from [Grafana Loki Example Dashboard](https://grafana.com/grafana/dashboards/13407).
   - Displays log data ingested by Loki.

2. **Prometheus Dashboard**:
   - Imported from [Grafana Prometheus Example Dashboard](https://grafana.com/grafana/dashboards/3662).
   - Displays system and application metrics gathered by Prometheus.


## Metrics Gathering

Prometheus has been extended to gather metrics from all services defined in the `docker-compose.yml` file. The following services are now being scraped:

- Prometheus itself (`localhost:9090`)
- Loki (`loki:3100`)
- Grafana (`grafana:3000`)
- Python App (`python_app:5000`)
- Go App (`go_app:8080`)

The `prometheus.yml` configuration has been updated to include these targets. Additionally, the Python and Go apps have been modified to expose metrics at the `/metrics` endpoint.

## Summary

The updates ensure that all services are equipped with log rotation mechanisms, memory constraints, and comprehensive monitoring through Grafana dashboards and Prometheus metrics. This enhances the overall reliability, observability, and efficiency of the system.