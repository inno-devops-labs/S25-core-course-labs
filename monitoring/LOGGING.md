# Logging Stack Documentation

## **Overview**

This document explains the **Loki + Promtail + Grafana** logging stack, detailing the role of each component, setap, and usage.

## **Components of the Logging Stack**

### **Loki (Log Aggregator & Storage)**

- **Loki is the central log storage system** that collects logs from multiple sources.
- Provides an **API for querying logs**.
- Accessible at `http://loki:3100`.

**Configuration File:** `loki-config.yml`
**Runs on Port:** `3100`

### **Promtail (Log Collector & Forwarder)**

- **Collects logs from `/var/log/*.log` and forwards them to Loki.**
- **Adds labels** (e.g., `{job="varlogs"}`) to help filter logs.

**Configuration File:** `promtail-config.yml`
**Runs on Port:** `9080`
**Sends logs to Loki at:** `http://loki:3100`

### **Grafana (Visualization & Querying)**

- **Grafana provides a UI to visualize logs from Loki.**
- Queries logs using **LogQL (Loki Query Language)**.
- Configured with Loki as a **data source**.
- Accessible at `http://localhost:3000`.

**Configuration File:** `docker-compose.yml`
**Runs on Port:** `3000`

---

## **Logging Workflow**

1. **Promtail** reads logs from `/var/log/*.log`.
2. **Promtail** sends logs to **Loki (`http://loki:3100`)**.
3. **Loki stores and indexes the logs** for fast search.
4. **Grafana queries Loki** and displays logs visually.

---

## **Screenshots**

### **Containers**

### **Grafana screenshot**
![Grafana Dashboard]()

