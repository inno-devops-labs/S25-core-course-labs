# Logging stack

## Components

The logging stack, which is used in this assignment, consists of three main components:

1. Loki
2. Promtail
3. Grafana

Let's consider each component in detail.

### Loki

Loki is the multiple-source log aggregation system, which is inspired by Prometheus. This system indexes only the metadata and stores unstructured compressed logs, which reduces operation costs and improves simplicity. \
In this particular case, it is used for log aggregation, query processing, and also as a datasource (source of logs) for Grafana.

I used the default config because there is no need in custom config for now.

![Loki config](./img/loki_config.png)

### Promtail

Promtail is the agent that collects logs from specified sources and sends them to Loki via its interface. Usually, this agent is running on every machine that contains operating applications, which should be monitored.
Promtail discovers targets, attaches labels and pushes them to Loki instance via API.

I used custom config because I need to specify the sources of logs that should be collected by Promtail.
In the config, I specified:

- the endpoint for logs pushing (`http://loki:3100/loki/api/v1/push`)
- `docker` backend configuration — it is used here for collecting the logs primarly from the Docker Compose project containers.
- `relabel_configs` - to label the logs by the container's name

![Promtail configuration](./img/promtail_config.png)

### Grafana

Grafana is an open source platform that allows to monitor and analyze data from various databases with a rich visualization functionality. \
In this particular case, we can use it for querying and viewing the logs.

I added Loki as the datasource by specifying its address and basic settings.

![Grafana datasources](./img/grafana_ds.png)

## Operation of logging stack

![Labels are loaded](./img/operating_1.png)
![Python app logs](./img/operating_2.png)
![Test query for Python app logs](./img/operating_3.png)

## Bonus task

### Extra app integration

I have extended the `docker-compose.yml` configuration to include my additional application.

![Extra app integration](./img/bonus_app.png)

### Collecting logs from all containers

I have configured Promtail to collect logs from all containers from `docker-compose.yml` file.

![Promtail configuration part that is responsible for collecting logs from all containers](./img/bonus_config.png)

![All containers logs](./img/bonus_1.png)
![Labels list](./img/bonus_2.png)
