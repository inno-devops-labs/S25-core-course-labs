# METRICS.md

## Prometheus Setup
- **Prometheus Overview**: Learned about Prometheus and its core concepts.
- **Docker Compose Integration**: Added Prometheus to `docker-compose.yml`.
- **Prometheus Configuration**: Configured Prometheus to scrape metrics from Loki and other services.
- **Targets Verification**: Verified targets at `http://localhost:9090/targets`.

![Prometheus Targets](screenshots/prometheus_targets.png)

---

## Grafana Dashboards
- **Prometheus Dashboard**: Created a dashboard to visualize metrics (e.g., request count, response time).
- **Loki Dashboard**: Created a dashboard to display application logs.

![Prometheus Dashboard](screenshots/prometheus_dashboard.png)
![Loki Dashboard](screenshots/loki_dashboard.png)

---

## Service Configuration Updates
- **Log Rotation**: Added log rotation mechanisms in `docker-compose.yml`.
- **Memory Limits**: Specified memory limits for all containers.

---

## Metrics Gathering
- Extended Prometheus to gather metrics from all services in `docker-compose.yml`.
