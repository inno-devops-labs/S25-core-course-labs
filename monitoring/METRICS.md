# Metrics Overview

The setup includes a Prometheus container that collects metrics from the prometheus, loki containers, and both the Python and Kotlin web applications. To enable metric collection, /metrics endpoints were added to the web apps with necessary middleware, allowing Prometheus to gather data.

## Logs and Screenshots

- [Prometheus Targets](logs2/targets.png)
- [Loki Dashboard](logs2/loki_dashboard.png)
- [Loki Prometheus](logs2/prometheus_loki.png)
- [Prometheus Dashboard](logs2/prometheus_dashboard1.png)
- [Python and Kotlin Metrics](logs2/prometheus_python_kotlin.png)
- [Prometheus Total Dashboard](logs2/prometheus_total_dashboard1.png)

Memory limits and log rotation settings were added to docker-compose.yml to optimize resource usage, with adjustments made for containers prone to out-of-memory issues. Health checks were also included to monitor the status of the applications.
