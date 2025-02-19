# Metrics via Prometheus

Installation includes a Prometheus container that collects metrics from Prometheus, a loki container and web applications written in Python and NodeJS.
In order to ensure the collection of metric data, `/metrics` endpoints have been added to web applications with the necessary intermediate production, which allows Prometheus to collect data.

# Key Functionalities:
1. **Networking**:
All services are connected to the monitoring network for inter-service communication.
2. **Health Checks**:
Each service has a healthcheck to ensure it's running correctly.
Uses `curl` to verify endpoints (`/ready`, `/health`, `/-/healthy`).
3. **Resource Limits**:
Memory limits are defined for each service (128M to 512M) to optimize resource usage.
4. **Logging Configuration**:
Python and Node.js apps use `json-file` logging with rotation (`max-size: 10m`, `max-file: 3`).

# Logs & Metrics
* [Loki-1](app-metrics/loki-dashboard1.png)
* [Loki-2](app-metrics/loki-dashboard2.png)
* [Loki-Prometheus](app-metrics/prometheus-loki.png)
* [NodeJS-App](app-metrics/prometheus-nodejs.png)
* [Python-App](app-metrics/prometheus-python.png)
* [Prometheus-Targets](app-metrics/prometheus-targets.png)
* [Prometheus-Overview-1](app-metrics/prometheus-overview1.png)
* [Prometheus-Overview-2](app-metrics/prometheus-overview2.png)
* [Prometheus-Metrics](app-metrics/prometheus-total.png)