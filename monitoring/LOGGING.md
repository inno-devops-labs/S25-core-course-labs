# Logging Stack Setup Report

## Stack Overview

This project uses the following logging stack:  
- **Grafana:** A tool for log visualization and analysis.  
- **Loki:** A system for log aggregation and storage.  
- **Promtail:** An agent that collects logs from the file system and sends them to Loki.  
- **Flask Application:** Our application running on port 5000, generating logs.  

## Configuration Description  

### `docker-compose.yml`  
The `docker-compose.yml` file defines four services:  
- **loki:** Uses the `grafana/loki` image and configuration from `loki-config.yaml`. Available on port `3100`.  
- **promtail:** Uses the `grafana/promtail` image and configuration from `promtail-config.yaml`. Scans log files in `/var/log`.  
- **grafana:** Provides a web interface for log visualization. Available on port `3000`. The administrator password is set via an environment variable.  
- **myapp:** Our Flask service, built from the `../app` folder (relative to the `monitoring` folder). The application runs on port `5000`.  

### `loki-config.yaml`  
The `loki-config.yaml` file contains the minimal configuration for running Loki. It includes server settings, ingester, storage schema, and configuration for storing logs on the local file system.  

### `promtail-config.yaml`  
The `promtail-config.yaml` file is configured to:  
- Listen on port `9080`.  
- Track positions in the `/tmp/positions.yaml` file.  
- Send logs to Loki at `http://loki:3100/loki/api/v1/push`.  
- Collect logs from files matching the pattern `/var/log/*.log` with the label `job: flask`.  

## Deployment and Testing  

1. **Build and start containers:**  
   Navigate to the `monitoring` folder and run:  


![Loki](loki.png)
