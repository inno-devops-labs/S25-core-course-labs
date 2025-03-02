# Metrics 

## Targets

List of all prometheus targets

![alt text](images/targets.png)

## Dashboards

Prometheus (using given example dashboard):

![alt text](images/prometheus_dashboard.png)

Loki (using given example dashboard):

![alt text](images/loki_dashboard.png)

## Service configuration updates

Added following lines for logging:

```
logging:
    driver: "json-file"
    options:
        max-size: "200k"
        max-file: "10"
```

Specified memory limit for each container by:

```
deploy:
    resources:
        limits:
        memory: 256M
```

## Python application metrics

![alt text](images/prometheus_python.png)


## Healthchecks

Implemented for python application container, for grafana and for loki
