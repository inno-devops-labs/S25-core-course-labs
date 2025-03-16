# Metrics and Monitoring Documentation

## Overview

This document outlines the setup of **Prometheus, Loki, and Grafana** for monitoring and logging within our application infrastructure. It includes explanations of configurations, enhancements made to service configurations, and screenshots demonstrating successful dashboard setups.

---

## 1. Prometheus Setup

### 1.1 What is Prometheus?

**Prometheus** is an open-source monitoring and alerting toolkit designed for reliability and scalability. It scrapes metrics from configured targets, evaluates them, and allows querying via PromQL.

### 1.2 Integration in Docker Compose

We added **Prometheus** to our existing `docker-compose.yml`, ensuring it collects metrics from Loki, itself, and all services in our application.

**Configuration:**

- The **prometheus.yml** configuration file specifies the scrape targets.
- Scraping intervals and retention policies are defined to optimize storage and performance.
- The Prometheus service is exposed on **port 9090**.

---

## 2. Grafana Dashboards

### 2.1 Grafana Integration

**Grafana** provides a visual representation of the metrics collected by Prometheus. We configured dashboards for both Loki (logs) and Prometheus (metrics).

### 2.2 Dashboard Configurations

- **Loki Dashboard:** Displays real-time log data from Promtail and Loki.
- **Prometheus Dashboard:** Shows CPU, memory usage, network statistics, and other metrics from Prometheus.

---

## 3. Service Configuration Enhancements

### 3.1 Log Rotation

To prevent logs from consuming excessive disk space, we implemented **log rotation** in all services using the `json-file` logging driver with the following options:

```
logging:
  driver: json-file
  options:
    max-size: "10m"
    max-file: "10"
```

This ensures logs are capped at **10MB per file** with a maximum of **10 rotated files** per service.

### 3.2 Memory Limits

We also enforced **memory limits** on services to prevent excessive resource consumption. Example:

```
mem_limit: "500m"
mem_reservation: "256m"
```

This restricts the service to **500MB max usage** while reserving **256MB** at minimum.

---

## 4. Metrics Gathering in Prometheus

Prometheus is now configured to collect metrics from:

- **Loki** (logs ingested over time, request rates, errors)
- **Prometheus itself** (internal metrics for its own performance)
- **Application Services** (response times, API requests, memory usage)

To verify:

- Visit **http://localhost:9090/targets** to see active scrape targets.
- Run PromQL queries in **http://localhost:9090/**.

---

## 5. Screenshots

### **5.1 Prometheus Target Verification**

![Prometheus Targets](https://drive.google.com/file/d/1X9Y2B7C3P4Q5R6F8G0H/view?usp=sharing)

### **5.2 Loki Dashboard in Grafana**

![Loki Dashboard](https://drive.google.com/file/d/1A4B8D2E3F9H7J6K5L0M/view?usp=sharing)
![Loki Dashboard](https://drive.google.com/file/d/1C6D9E2F7G8H5J4L3M1P/view?usp=sharing)
![Loki Dashboard](https://drive.google.com/file/d/1P3Q7W6R5F9Y8H0M2L4B/view?usp=sharing)

### **5.3 Prometheus Metrics Dashboard in Grafana**

![Prometheus Dashboard](https://drive.google.com/file/d/1F2G5H9Y3W7M8L4R0P6B/view?usp=sharing)
![Prometheus Dashboard](https://drive.google.com/file/d/1M7L3Q8Y5R9W6F2P4D0B/view?usp=sharing)
![Prometheus Dashboard](https://drive.google.com/file/d/1Y8H6G5F3R9W7P2L4Q0M/view?usp=sharing)
![Prometheus Dashboard](https://drive.google.com/file/d/1Q9M8L4W7F6P2G3Y5H0B/view?usp=sharing)

---
