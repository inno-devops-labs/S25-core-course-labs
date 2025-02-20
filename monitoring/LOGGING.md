# Logging Stack: Promtail, Loki, and Grafana

## Overview
This logging stack provides centralized logging and visualization using **Promtail, Loki, and Grafana**. The goal is to collect logs from **containers and system logs**, store them in **Loki**, and visualize them using **Grafana**.

## Components

### **1 Loki (Log Aggregator)**
- **Purpose:** Stores and indexes logs.
- **Runs on Port:** `3100`
- **Data Flow:** 
  - Receives logs from **Promtail**.
  - Provides log querying via API (`http://localhost:3100`).

### **2 Promtail (Log Collector)**
- **Purpose:** Collects logs from **Docker containers** and **system logs (`/var/log/` directory)**.
- **Configuration File:** `config.yaml`
- **Data Flow:**
  - Reads logs from **containers and system logs**.
  - Sends logs to **Loki** (`http://loki:3100/loki/api/v1/push`).

### **3 Grafana (Visualization)**
- **Purpose:** Visualizes logs stored in **Loki**.
- **Runs on Port:** `3000`
- **Default Login:**
  - Username: `admin`
  - Password: `admin`
- **Data Flow:**
  - Queries logs from **Loki**.
  - Displays logs using dashboards and queries.

---

## ** Deployment Instructions**
### **1️ Start the Logging Stack**
Run the following command:
```sh
docker-compose up -d --force-recreate --build
```

### **📸 Screenshot: Logs in Grafana**
![Grafana Logs](screenshots/screen1.png)

### **📸 Screenshot: Promtail Running**
![Promtail Logs](screenshots/screen2.png)

