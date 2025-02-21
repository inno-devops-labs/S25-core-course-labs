# Metrics

## Prometheus Targets

Set up targets for Loki and Prometheus containers:

<img width="1470" alt="prom-targets" src="https://github.com/user-attachments/assets/c7389c1e-aec1-4ad3-b966-6e2efcf04ae1" />

## Grafana Dashboards

<img width="1470" alt="Снимок экрана 2025-02-21 в 22 22 36" src="https://github.com/user-attachments/assets/19f8cbfc-0b20-4c65-85b0-69fc0f6eec8f" />

<img width="1470" alt="Снимок экрана 2025-02-21 в 22 23 03" src="https://github.com/user-attachments/assets/1e20e150-21e3-455b-ada1-35b1430253ea" />

## Log Rotation

To prevent excessive log growth, all services now use **log rotation**:

- Maximum log file size: **10MB**
- Maximum number of log files: **3**

Configuration in `docker-compose.yml`:

```yaml
logging:
  driver: "json-file"
  options:
    max-size: "10m"
    max-file: "3"
```

## Memory Limits

Each service now has defined **memory usage limits** to improve system stability:

- **Loki, Grafana, Prometheus:** `512MB`
- **Promtail, Moscow-time-app, Omsk-time-app:** `256MB`

Configuration:

```yaml
deploy:
  resources:
    limits:
      memory: 512M
```

### Prometheus Metrics Collection

Prometheus is configured to scrape metrics from all services. The updated `prometheus.yml` includes:

```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: "prometheus"
    static_configs:
      - targets: ["prometheus:9090"]

  - job_name: "loki"
    static_configs:
      - targets: ["loki:3100"]

  - job_name: "grafana"
    metrics_path: "/metrics"
    static_configs:
      - targets: ["grafana:3000"]

  - job_name: "moscow-time-app"
    metrics_path: "/metrics"
    static_configs:
      - targets: ["moscow-time-app:8080"]

  - job_name: "omsk-time-app"
    metrics_path: "/metrics"
    static_configs:
      - targets: ["omsk-time-app:8081"]
```
