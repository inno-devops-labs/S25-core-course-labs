# Metrics

## Targets

![Targets](assets/prometheus-targets.png)

## Loki Dashboard

![Loki Dashboard](assets/loki-dashboard.png)

## Prometheus Dashboard

![Prometheus Dashboard](assets/prometheus-dashboard.png)

## Log Rotation and Memory Limit

1. Log rotation is configured with `json-file` driver with `max-size` and `max-file` options.
2. Memory limit is restricted for each container:
  - *Prometheus*: 1g
  - *Loki* & *Grafana*: 512m
  - *Promtail* and applications: 256m
