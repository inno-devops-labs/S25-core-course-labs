# Prometheus & Grafana Setup

## **1. Prometheus Overview**

Prometheus is a monitoring system that collects and queries metrics.

## **2. Screenshots**

### **Prometheus Targets**


### **Grafana Loki Dashboard**


### **Grafana Prometheus Dashboard**


## **3. Log Rotation and Memory Limits**

### **Log Rotation Settings**
- **Maximum Log File Size:** `10MB`
- **Number of Rotated Files:** `3`
- **Log Driver:** `json-file`

```yaml
logging:
  driver: "json-file"
  options:
    max-size: "10m"
    max-file: "3"

