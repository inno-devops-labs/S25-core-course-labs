# Logging Stack Report
##### This document provides a detailed explanation of the logging stack setup, including the roles of each component and how they interact to collect, store, and visualize logs.

### Overview
The logging stack consists of three main components: Promtail , Loki , and Grafana . These tools work together to collect logs from Docker containers, store them in a centralized location, and provide a user-friendly interface for querying and visualizing the logs.

### Components
1. Promtail  
 - Role : Log Collector
Promtail is responsible for collecting logs from Docker containers and sending them to Loki for storage. It uses the Docker API to discover running containers and collects their logs.  
 - Key Features:  
 - Log Collection : Promtail scrapes logs from Docker containers and system logs (e.g., /var/log).  
 - Labeling : Promtail adds metadata (labels) to logs, such as container names, log streams, and custom labels.  
 - File Position Tracking : Promtail tracks the position of logs it has already read using a positions.yaml file, ensuring no logs are missed or duplicated.  
 - Docker API : Promtail connects to the Docker socket (/var/run/docker.sock) to discover containers and collect their logs.  
 - Relabeling : Logs are enriched with metadata (e.g., container name, log stream) before being sent to Loki.

---

2. Loki  
 - Role : Log Aggregator and Storage  
Loki is a horizontally scalable, highly available, multi-tenant log aggregation system inspired by Prometheus. It stores logs and provides an API for querying them.  
 - Key Features:
 - Log Storage : Loki stores logs in a compressed format, making it efficient for large-scale log collection.
 - Label-Based Indexing : Logs are indexed by labels (metadata), which allows for efficient querying.
 - Retention : Loki can be configured to retain logs for a specific period (e.g., 7 days, 30 days).
 - Clients : Loki accepts logs from Promtail via the /loki/api/v1/push endpoint.
 - Retention Period : Logs are stored for a configurable duration (e.g., retention_period: 720h).

---

3. Grafana  
 - Role : Log Visualization  
Grafana is used to query and visualize logs stored in Loki. It provides a user-friendly interface for exploring logs and creating dashboards.  
 - Key Features:  
 - Data Source Integration : Grafana connects to Loki as a data source to query logs.  
 - Log Querying : Users can query logs using label-based filters.  
 - Visualization : Grafana allows users to create dashboards and alerts based on log data.  
 - Automatic Provisioning : Grafana is pre-configured to connect to Loki as the default data source.  
 - Anonymous Access : Grafana is configured to allow anonymous access for easier testing and exploration.

### How the Stack Works  
 - Log Collection :  
Promtail runs as a sidecar container and collects logs from Docker containers via the Docker API.  
It also collects logs from system directories like /var/log.  
 - Log Enrichment :  
Promtail enriches logs with metadata (labels) such as container name, log stream, and custom labels.  
Logs are sent to Loki in batches via the /loki/api/v1/push endpoint.  
 - Log Storage :  
Loki receives logs from Promtail and stores them in a compressed format.  
Logs are indexed by labels, allowing for efficient querying.  
 - Log Visualization :  
Grafana connects to Loki as a data source.  
Users can query logs using label-based filters.  
Logs are displayed in a user-friendly interface, and users can create dashboards for monitoring.

---

![image](https://github.com/UTKANOS-RIBA/S25-core-course-labs/Lab7/monitoring/image.png)
