# Monitoring with Prometheus

## Task 1: Prometheus Setup

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

## Task 2: Dashboard and Configuration Enhancements

### Grafana Dashboards

I have downloaded Loki and Prometheus dashboards in JSON format and put them into `/var/lib/grafana/dashboards` directory. \
Also I have specified the `GF_DASHBOARDS_DEFAULT_HOME_DASHBOARD_PATH` variable that allows to open some dashboard by default on home page. I used Loki dashboard as a default one.

I added Prometheus as another datasource for Grafana.

![Updated Grafana config](./img/dashboards_grafana.png)

Here are the screenshots displaying successful dashboard configurations.

![Dashboards list](./img/dashboards_list.png)

#### Loki dashboard

![Loki dashboard 1](./img/dashboards_loki_1.png)
![Loki dashboard 2](./img/dashboards_loki_2.png)

#### Prometheus dashboard

![Prometheus dashboard 1](./img/dashboards_prom_1.png)
![Prometheus dashboard 2](./img/dashboards_prom_2.png)

### Service Configuration Updates:

I have added log rotation mechanisms and memory limits for all containers in `docker-compose.yml` (added config to corresponding services).

For log rotation, I have specified the max number of files for rotation (3) and max size for these files (10 Mb). As for memory limits, I specified 256 Mb for my applications services, and 1 Gb for logging stack services.

![256m conf](./img/updateconf_256m.png)
![1g conf](./img/updateconf_1g.png)
