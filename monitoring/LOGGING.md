# Logging Stack Overview

## Components

![image](https://github.com/user-attachments/assets/bc6da33c-deb2-4f36-ac62-452cf59e4c4a)

### Loki <img src="https://github.com/user-attachments/assets/d349e1ca-abc3-4d05-945a-dbcdbfaa5a23" alt="image" width="22">

**Role:** Loki is a log aggregation system designed for efficiency and cost-effectiveness. It stores logs and provides a query interface for retrieving them.

**Configuration:**

- Runs as a Docker container on port `3100`.
- Stores log data in the `loki-data` volume.
- Uses a configuration file `/etc/loki/local-config.yaml`.

### Promtail <img src="https://github.com/user-attachments/assets/4893fff4-d0f7-476e-8a49-2258814b9c03" alt="image" width="30">

**Role:** Promtail is a log shipper that collects logs from Docker containers and forwards them to Loki.

**Configuration:**

- Mounts `/var/run/docker.sock` to access Docker logs.
- Uses `promtail-config.yml` to define log scraping rules.
- Configured to auto-discover Docker containers and extract labels (`app`, `logging=true`, etc.).
- Sends logs to Loki at `http://loki:3100/loki/api/v1/push`.

### Grafana <img src="https://github.com/user-attachments/assets/54e45b10-ae22-4aec-bc9d-839f3fc6a521" alt="image" width="22">

**Role:** Grafana is a visualization tool that provides a user interface for querying and analyzing logs stored in Loki.

**Configuration:**

- Runs on port `3000`.
- Uses `grafana-datasources.yml` to configure Loki as the default data source.
- Authentication is managed via environment variables (`admin/admin`).
- Stores dashboard configurations in `grafana-data` volume.

### Monitored Applications

Two applications (`moscow-time-app` and `omsk-time-app`) are running in the logging stack:

- These applications are labeled with `logging=true` to indicate that their logs should be collected.
- Logs are scraped by Promtail and sent to Loki.

<img width="1470" alt="Снимок экрана 2025-02-21 в 20 36 23" src="https://github.com/user-attachments/assets/ee73e10e-8e76-474f-bc0f-01cd502461d4" />

<img width="1470" alt="Снимок экрана 2025-02-21 в 20 30 13" src="https://github.com/user-attachments/assets/e15b449c-1750-45bf-bca8-728939cebb54" />

## Network and Storage

- All services communicate over the `monitoring` network (Docker bridge).
- Persistent volumes (`loki-data`, `grafana-data`) are used to store logs and dashboards.

## Data Flow

1. **Log Generation:** Applications generate logs.
2. **Log Collection:** Promtail scrapes logs from Docker containers.
3. **Log Storage:** Logs are sent to Loki for storage and indexing.
4. **Log Visualization:** Grafana queries Loki and visualizes logs in dashboards.

This setup ensures efficient log aggregation, storage, and visualization, providing insights into application behavior and system health.
