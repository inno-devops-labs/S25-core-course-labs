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

## Prometheus Metrics Collection

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
      - targets: ["omsk-time-app:4567"]
```

## Application Metrics

### Python app

<img width="1470" alt="Снимок экрана 2025-02-22 в 01 49 45" src="https://github.com/user-attachments/assets/a4831e61-676b-4e96-8550-7df8cd22b22f" />

### Ruby app

<img width="1470" alt="Снимок экрана 2025-02-22 в 01 50 22" src="https://github.com/user-attachments/assets/4b9666e4-8e18-486b-9a3c-77176d429f4e" />

## Targets

![image](https://github.com/user-attachments/assets/ff368f9e-bba2-41d7-8c95-091a42d5fd33)

## Health Checks

```bash
CONTAINER ID   IMAGE                           COMMAND                  CREATED         STATUS                   PORTS                    NAMES
76500886e596   grafana/grafana:latest          "/run.sh"                2 minutes ago   Up 2 minutes (healthy)   0.0.0.0:3000->3000/tcp   monitoring-grafana-1
1221174d217a   grafana/promtail:latest         "/usr/bin/promtail -…"   2 minutes ago   Up 2 minutes                                      monitoring-promtail-1
2601ad899374   ebob/moscow-time:v1.1           "gunicorn -w 4 -b 0.…"   2 minutes ago   Up 2 minutes (healthy)   0.0.0.0:8080->8080/tcp   moscow-time-app
c88b7b114f7a   ebob/omsk-time:v1.1             "ruby app.rb"            2 minutes ago   Up 2 minutes (healthy)   0.0.0.0:8081->4567/tcp   omsk-time-app
452a99ba7497   prom/prometheus:latest          "/bin/prometheus --c…"   2 minutes ago   Up 2 minutes (healthy)   0.0.0.0:9090->9090/tcp   monitoring-prometheus-1
818f468a006a   grafana/loki:latest             "/usr/bin/loki -conf…"   2 minutes ago   Up 2 minutes (healthy)   0.0.0.0:3100->3100/tcp   monitoring-loki-1
```

Modify docker-compose.yml file with:

```yml
healthcheck:
      test: ["CMD", "wget", "-q", "--spider", "http://0.0.0.0:8080"]
      interval: 30s
      timeout: 10s
      retries: 3
```
