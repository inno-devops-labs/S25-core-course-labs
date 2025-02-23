# Monitoring

## Task 1

I have added Prometheus monitoring with the following configuration:

- Running on port 9090
- Using the official `prom/prometheus:latest` image
- Configured with a memory limit of 512MB
- Mounted prometheus.yml configuration file which scrapes metrics from:
  - Prometheus itself (localhost:9090)
  - Loki (port 3100)
  - Python web app (port 8000)
  - Grafana (port 3000)
  - Promtail (port 9080)

You can verify Prometheus is running correctly by checking the screenshot.

![Prometheus Running](screenshots/prometheus-running.png)

## Task 2

### - Setup Dashboard

- Loki Dashboard

![Loki Dashboard](screenshots/loki-dash.png)

- Prometheus Dashboard

![Prometheus Dashboard](screenshots/prometheus-dashboard.png)

### - Configuration Details

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

### - Metric Gathering

I have extended the metric gathering to include other services.

![Metrics](screenshots/extended_metric_gathering.png)


