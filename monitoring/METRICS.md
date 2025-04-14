# Monitoring and Metrics with Prometheus

In this document, I'll outline the monitoring solution I've implemented using Prometheus, Loki, and Grafana for my applications.

## Overview

For my monitoring solution, I've integrated several components that work together to provide comprehensive visibility into my applications:

- **Prometheus**: I'm using this to collect and store metrics from all services
- **Loki**: This aggregates and indexes logs from my applications
- **Promtail**: I've deployed this to collect logs and forward them to Loki
- **Grafana**: I'm using this to create dashboards that visualize metrics and logs
- **Node Exporter**: I've added this to expose host-level metrics

With this setup, I can monitor both my infrastructure and applications, giving me insights into performance, resource usage, and potential issues as they arise.

## Monitoring Stack Components

### Prometheus

I chose Prometheus as my monitoring platform because it's an open-source monitoring and alerting toolkit designed for reliability and scalability. It collects metrics from configured targets at specified intervals, evaluates rule expressions, displays results, and can trigger alerts when certain conditions are met.

What I like about Prometheus:
- It has a multi-dimensional data model with time series data identified by metric name and key/value pairs
- PromQL offers a flexible query language for data analysis
- It doesn't rely on distributed storage; single server nodes are autonomous
- It collects time series via a pull model over HTTP
- It supports pushing time series through an intermediary gateway
- It can discover targets via service discovery or static configuration

### Loki

For log management, I implemented Loki, which is a horizontally-scalable, highly-available, multi-tenant log aggregation system inspired by Prometheus. I chose it because it's cost-effective and easy to operate—it doesn't index the contents of the logs but rather a set of labels for each log stream.

### Promtail

To collect logs, I'm using Promtail as an agent that ships the contents of local logs to my Loki instance. I've deployed it to every machine that has applications I need to monitor.

### Grafana

For visualization, I'm using Grafana, which allows me to query, visualize, alert on, and explore my metrics no matter where they're stored.

## Prometheus Setup

### Configuration

I've created a Prometheus configuration file (`prometheus.yml`) that defines how it scrapes metrics from various targets:

```yaml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

scrape_configs:
  - job_name: "prometheus"
    static_configs:
      - targets: ["localhost:9090"]

  - job_name: "node"
    static_configs:
      - targets: ["node-exporter:9100"]

  - job_name: "loki"
    static_configs:
      - targets: ["loki:3100"]

  - job_name: "grafana"
    static_configs:
      - targets: ["grafana:3000"]

  - job_name: "python-app"
    metrics_path: /metrics
    static_configs:
      - targets: ["python-app:3000"]

  - job_name: "node-app"
    metrics_path: /metrics
    static_configs:
      - targets: ["node-app:3001"]
```

## Service Configuration Enhancements

### Log Rotation

I've configured log rotation for all services in my Docker Compose to prevent excessive disk usage:

```yaml
logging:
  driver: "json-file"
  options:
    max-size: "10m"
    max-file: "3"
```

This configuration limits my log files to 10MB in size and keeps a maximum of 3 files per service, which helps me manage disk space efficiently.

### Memory Limits

To ensure resource efficiency, I've added memory limits to all services:

```yaml
mem_limit: 256M
```

I've set different limits based on each service's requirements:
- For core services like Prometheus, Loki, and Grafana: 256MB
- For lighter services like Promtail and Node Exporter: 128MB
- For my application containers: sized according to their specific needs

## Application Metrics

I've instrumented my applications to expose Prometheus metrics, giving me insights into their performance and behavior.

### Python App Metrics

In my Python Flask application, I've added metrics for:

- Request counts by endpoint
- Response latency
- Application uptime

These metrics help me understand how my Python application is performing and identify potential bottlenecks.

### Node.js App Metrics

For my Node.js application, I've implemented metrics through the prom-client library, including:

- HTTP request counts
- Request duration histograms
- Node.js-specific metrics (memory usage, event loop lag, etc.)

These metrics give me a comprehensive view of my Node.js application's performance.

## Health Checks

I've implemented health checks for all services in my Docker Compose configuration:

```yaml
healthcheck:
  test: ["CMD-SHELL", "wget --no-verbose --tries=1 --spider http://localhost:3000/api/health || exit 1"]
  interval: 30s
  timeout: 5s
  retries: 3
  start_period: 10s
```

I've customized each health check command according to each service's API or functionality:

- For my web applications: checking the application's health endpoint
- For Prometheus: checking the `-/healthy` endpoint
- For Loki and Promtail: checking the `/ready` endpoint
- For Grafana: checking the `/api/health` endpoint

These health checks allow Docker to automatically restart containers if they become unhealthy, improving the overall reliability of my monitoring stack.