# METRICS.md

## Components
- **Loki:** For log aggregation.
- **Promtail:** For collecting and shipping logs.
- **Grafana:** For dashboard visualization.
- **Prometheus:** For scraping and collecting metrics.
- **app_python:** A Python application exposing its metrics.

## Prometheus Setup

### Prometheus Configuration
The `prometheus.yml` file is configured as follows:
- **Global Settings:**
  The `scrape_interval` is set to `15s`, meaning Prometheus will collect metrics every 15 seconds.
- **Scrape Configurations:**
  Four jobs are defined:
  - **prometheus:** Scrapes metrics from Prometheus itself (`localhost:9090`).
  - **loki:** Scrapes metrics from Loki at `loki:3100`.
  - **grafana:** Scrapes metrics from Grafana at `grafana:3000`.
  - **app_python:** Scrapes metrics from our Python application at `app_python:5000`.

http://localhost:9090/targets:

Grafana Prometheus Dashboard:

Grafana Loki Dashboard:


For the app_python service, log rotation is configured to prevent logs from consuming excessive disk space:

Driver: json-file
Options:
max-size: "10m" – Each log file is limited to 10MB.
max-file: "3" – Up to 3 log files are retained.

The app_python container is restricted to 512MB of memory to ensure it does not consume excessive resources.
