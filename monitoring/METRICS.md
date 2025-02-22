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
![image](https://github.com/user-attachments/assets/f7406f9e-f1db-4270-9e15-e05ca48c0b79)

Grafana Prometheus Dashboard:
![image](https://github.com/user-attachments/assets/d1bc1a63-eb62-4e98-9040-7c08f2e286d3)

Grafana Loki Dashboard:
![image](https://github.com/user-attachments/assets/531d6264-35b0-4377-9dc3-836f14e25c7e)


For the app_python service, log rotation is configured to prevent logs from consuming excessive disk space:

Driver: json-file
Options:
max-size: "10m" – Each log file is limited to 10MB.
max-file: "3" – Up to 3 log files are retained.

The app_python container is restricted to 512MB of memory to ensure it does not consume excessive resources.
