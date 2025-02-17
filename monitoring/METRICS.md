# Prometheus & Grafana Setup

## **1. Prometheus Overview**

Prometheus is a monitoring system that collects and queries metrics.

## **2. Screenshots**

### **Prometheus Targets**

![Prometheus Targets](https://github.com/user-attachments/assets/c219e1e6-1b37-4a37-94a2-df0350832b9a)

### **Grafana Loki Dashboard**

![Loki dashboard](https://github.com/user-attachments/assets/cc617edf-0796-4890-912d-56db60c5b635)

### **Grafana Prometheus Dashboard**

![Prometheus dashboard](https://github.com/user-attachments/assets/86cb66a7-53da-465c-b708-1efff6f3457b)

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

