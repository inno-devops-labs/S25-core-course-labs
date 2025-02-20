# Monitoring with Prometheus

## Prometheus Setup

### Prometheus Configuration

I have expanded my existing `docker-compose.yml` from the previous lab to include Prometheus.

![Prometheus in docker-compose.yml](./img/prometheus_1.png)

I configured Prometheus to collect metrics from both Loki and Prometheus containers by using a custom config.

![Prometheus config](./img/prometheus_2.png)

### Verify Prometheus Targets

Here are the screenshots that confirm the successful setup.

![Target health](./img/prometheus_3.png)

![Loki query results](./img/prometheus_4.png)

![Prometheus query results](./img/prometheus_5.png)
