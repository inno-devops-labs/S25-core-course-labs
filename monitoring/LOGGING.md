# Logging Stack Report

## Stack Components

### Loki

It is a scalable log aggregator. It indexes logs and stores them in a time-series database.

It listens on port `3100` for incoming log data. Logs are stored persistently in the `loki-data` volume.

### Promtail

It is an agent that collects logs from the Docker container and forwards them to Loki. It scrapes log files using the given config.

`promtail.yml` file is configured to scrape logs from the Docker container and forward them to Loki.

### Grafana

Grafana provides UI for the logging stack. It queries Loki for log data and shows dashboards and query results.

It listens on **port** `3000` and is accessible without authentication.

## Screenshots

Start using docker compose up:

![Docker Compose](./img/docker_compose_up.png)

Browser App Python:

![Browser App Python](./img/browser_app_py.png)

Browser App Go:

![Browser App Go](./img/browser_app_go.png)

Grafana Main Page:

![Grafana Main](./img/grafana_main.png)

Grafana Data Sources:

![Grafana Data Sources](./img/grafana_datasources.png)

Grafana Logs Grafana:

![Grafana Logs Grafana](./img/grafana_logs_grafana.png)

Grafana Logs Loki:

![Grafana Logs Loki](./img/grafana_logs_loki.png)

Grafana Logs Promtail:

![Grafana Logs Promtail](./img/grafana_logs_promtail.png)

Grafana Logs Python:

![Grafana Logs Python](./img/grafana_logs_py.png)

Grafana Logs Go:

![Grafana Logs Go](./img/grafana_logs_go.png)
