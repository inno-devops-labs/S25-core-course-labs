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

- **Reads logs from systemd-journal (/var/log/journal/).**
- **Forwards logs to Loki (http://loki:3100).**
- **Adds labels** to help filter logs.

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

## **Logging Workflow**

1. **Promtail** collects logs from systemd-journal (/var/log/journal/).
2. **Promtail** sends logs to **Loki (`http://loki:3100`)**.
3. **Loki stores and indexes the logs** for fast search.
4. **Grafana queries Loki** and displays logs visually.

## **Screenshots**

### **Containers**

![Containers](https://github.com/user-attachments/assets/926fd045-a623-49af-bf0c-65d7e14bfb45)

### **Grafana screenshot**

![Grafana](https://github.com/user-attachments/assets/bcae0feb-3611-40fb-82f8-2c5000cc8547)
![Grafana](https://github.com/user-attachments/assets/6d1746f0-a318-4756-b7dc-1caf1c1af8bf)
