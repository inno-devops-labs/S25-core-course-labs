# Logging

### Promtail

Promtail scrapes log files as specified in the `promtail-config.yml`
file and forwards them to Loki for storage.

### Loki

Loki indexes incoming log streams and stores them in a time-series database.
It listens for log input on port `4000`.

### Grafana

Grafana connects to Loki as a data source,
enabling users to view dashboards and run queries on log data.
Grafana is accessible via port `3000`.

## Screenshots

Python Web Application in Browser:

![Python Application](./screenshots/app_python.png)

Start with Docker Compose:

![Docker Compose](./screenshots/docker_compose.png)

Grafana Home Page:

![Grafana Home](./screenshots/grafana_home.png)

Grafana Data Sources Configuration:

![Grafana Data Sources](./screenshots/grafana_sources.png)

Grafana Logs - Grafana Service:

![Grafana Logs - Grafana](./screenshots/grafana_service.png)

Grafana Logs - Loki Service:

![Grafana Logs - Loki](./screenshots/loki_service.png)

Grafana Logs - Promtail Service:

![Grafana Logs - Promtail](./screenshots/promtail_service.png)