# Monitoring Setup Documentation

## Prometheus Setup

### Prometheus Targets

![Prometheus Targets](./attachments/prometheus.png)

### Prometheus Configuration

The Prometheus configuration includes scraping metrics from:

- Prometheus itself
- Loki
- Grafana

## Grafana Dashboards

### Loki Dashboard

![Loki Dashboard](./attachments/loki-dash.png)

### Prometheus Dashboard

![Prometheus Dashboard](./attachments/prometheus-dash-1.png)

![Prometheus Dashboard](./attachments/prometheus-dash-2.png)

## Service Configuration Updates

### Log Rotation

All services in the docker-compose.yml file have been configured with log rotation:

```yaml
logging:
  driver: "json-file"
  options:
    max-size: "10m"
    max-file: "3"
```

### Memory Limits

All containers have been assigned memory limits:

```yaml
mem_limit: 512m
```
