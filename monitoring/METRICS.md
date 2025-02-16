# Metrics

## Task 1: Prometheus Setup

`Prometheus` with captured logs:

![Prometheus UI screenshot](misc/prometheus_task_1.png)

## Task 2: Dashboards and Configuration Enchancements

### Dashboards

`Grafana` with `Prometheus` dashboard

![Dashboard for `Prometheus`](misc/dashboard_prometheus.png)

`Grafana` with `Loki` dashboard

![Dashboard for `Loki`](misc/dashboard_loki.png)

### Service Configuration Updates

I configured log rotation mechanism with

```yaml
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
```

for all services and set resource limits

```yaml
    deploy:
      resources:
        limits:
          memory: 128M
```

For web applications and `Promtail` memory limit is `128M`,
for `Grafana`, `Loki`, and `Prometheus` memory limit is `512M`.

### Metrics Gathering

I extend `Prometheus` config to capture log from web applications:

```yml
# begining from `prometheus.yml`

  - job_name: 'promtail'
    static_configs:
      - targets: ['promtail:9080']

  - job_name: "grafana"
    static_configs:
      - targets: ["grafana:3000"]

```

![Web application metrics](misc/prometheus_task_2.png)

## Bonus task

- TODO
