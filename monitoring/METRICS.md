# Metrics

This report provides results of the lab with demonstration of screenshots.

## Task 1

In this step service `prometheus` was introduced into `docker-compose.yml`. Process of configuration is similar to the previous lab (check services `grafana` and `promtail`). The result you may see on the screenshot.

![Loki and Prometheus](img/loki_and_prometheus_monitoring.png)
![Loki's metric](img/loki_metric.png)
![Prometheus' metric](img/prometheus_metric.png)

## Task 2

Dashboards from examples (![Loki](https://grafana.com/grafana/dashboards/13407-loki2-0-global-metrics/) and ![Prometheus](https://grafana.com/grafana/dashboards/3662-prometheus-2-0-overview/)) was used. The process was simple (just importing, using UI, which is intuitive). Metrics for other services was introdiced. There are results:

**Loki**:

![Loki](img/loki_overview_1.png)
![Loki](img/loki_overview_2.png)
![Loki](img/loki_overview_3.png)

**Prometheus:**
![Prometheus](img/prometheus_overview_1.png)
![Prometheus](img/prometheus_overview_2.png)
![Prometheus](img/prometheus_overview_3.png)
![Prometheus](img/prometheus_overview_4.png)
![Prometheus](img/prometheus_overview_5.png)
![Prometheus](img/prometheus_overview_6.png)

**Other services' metrics:**

![Grafana's metric](img/grafana_metric.png)
![Promtail's metric](img/promtail_metric.png)

Log rotation mechanism realised by introducing

```yaml
    logging:
      driver: "json-file"
      options:
        max-size: "10m"  
        max-file: "3"
```

for each component in `docker-compose.yml`.

For memory limits was used

```yaml
    mem_limit: 512m
```

Finally, all services was gathered (python_app from bonus task too)

![All services](img/all_services.png)

## Bonus task

**Metrics:**

![Python app's metric](img/python_app_metric.png)

**Health check:**

Was introduced

```yaml
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:<port>/<url's tail>"]
      interval: <interval>s
      timeout: <timeout>s
      retries: <retries>
      ```

for each service.
