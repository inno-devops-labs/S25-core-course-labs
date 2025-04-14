# Metrics

## Overview

I did the tasks a little bit out of order. I have exported metrics from code and exposed a special endpoint in my applications. Then I added a prometheus container to the `docker-compose.yml`, and created a configuration file for it. After that I added the log rotation and memory limit specifications and ended everything up with healthchecks.

## Prometheus status

Below you may see that all the services are up and healthy

![prometheus status](/monitoring/media/prom.png)

## Dashboards

Here are presented the `prometheus` and `loki` dashboards.

### Prometheus

![prometheus](/monitoring/media/prom_dashboard.png)

### Grafana

![loki](/monitoring/media/loki_dashboard.png)

## Application metrics

There are some metrics displayed by applications and collected by prometheus

### Moscow Time App

![moscow prom](/monitoring/media/moscow_prom.png)

### Url Shortener App

![url prom](/monitoring/media/url_prom.png)

## Log Rotations and Memory Limits

I decided to have same log rotations and memory limits for all containers, declared them in one place and used everywhere else.

```yaml
x-logging:
  &my-logging
  driver: "json-file"
  options:
    max-size: "200k"
    max-file: "10"
    tag: "{{.ImageName}}|{{.Name}}"

x-deploy:
  &my-deploy
  resources:
    limits:
      memory: 512M
```

## Health checks

For health checks I used tools like curl and wget to send a request. Here is an example of it:

```yaml
healthcheck:
      test: ["CMD-SHELL", "curl --fail http://localhost:8080/manage || exit 1"]
      interval: 10s
      timeout: 5s
      retries: 5
```
