# Lab 7: Monitoring and Logging - Task 2: Documentation and Reporting
The main components are:

Grafana:
A visualization and analytics platform that provides dashboards to monitor and query your logs.

Loki:
A log aggregation system that indexes and stores logs efficiently. It is designed to work seamlessly with Grafana to query logs.

Promtail:
An agent that collects logs from your host (or containers) and sends them to Loki.

## Docker Compose Setup
The logging stack and the application are defined in the `docker-compose.yaml` file
Key Points:
Service Dependencies:
Promtail waits for Loki to be ready, and Grafana depends on Loki, ensuring the logging backend is available when needed.
Persistent Volumes:
Data for Loki and Grafana is persisted using named volumes (loki_data and grafana_data).
The Promtail configuration is defined in promtail-compose.yaml
The Loki configuration is defined in loki-config.yaml

##Testing and Verification
'''
docker-compose up -d
'''
go to  http://localhost:3000
log in via admin / admin 

![image](https://github.com/user-attachments/assets/c83774ea-f9a2-402d-a1d6-817599537eb4)


