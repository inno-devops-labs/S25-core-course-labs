# Metrics with Prometheus

Firstly, we need to run docker compose
```
docker-compose up -d
```

![up docker metrics](./images/up_metrics.png)


I've configured endpoint `/metrics` in both Python and JS applications
## Targets

![prometheus targets](./images/targets.png)


#### Also, we can check metrics of `app_python`

![python metrics](./images/py_metrics.png)

#### And for `app_js`

![js metrics](./images/js_metrics.png)


# Dashboards

## Loki

![loki metrics dash board](./images/loki_metrics.png)


## Prometheus

![prometheus metrics](./images/prometh_metrics/init.png)

#### and further info:

![first statistics img](./images/prometh_metrics/1.png)
![second statistics img](./images/prometh_metrics/2.png)


# Health checks


### Grafana
I used `curl` to try access `localhost:3000`

### Loki
I used `pgrep` to grep `promtail`

### Prometheus
I used `wget` to access `localhost:9090/-/healthy`

### My apps
I used specially created `/health` endpoint in each of the apps and 
a command `curl` to get access to this endpoint to cheack whether
the app is running or not

### Verify health check with `docker ps`
![health check of containers](./images/healthcheck.png)
