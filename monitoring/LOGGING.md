# Logging Stack Report

## Overview

The stack comprises three primary components—**Loki**, **Promtail**, and **Grafana**—which together enable centralized collection, storage, and visualization of container logs. In addition, the configuration has been extended (bonus task) to include an extra application for comprehensive logging across all services.

## Components

### Loki

- **Role:**  
  Loki is the backend log aggregation system. It stores and indexes logs sent by Promtail, making them queryable via Grafana.
- **Configuration:**  
  - Runs on port **3100**.
  - Configured with a local configuration file.
  - Receives logs at the endpoint: /loki/api/v1/push.

### Promtail

- **Role:**  
  Promtail acts as a log collector. It scrapes logs from Docker containers and forwards them to Loki.
- **Configuration Details:**
  - **Positions File:**  
    Tracks which log entries have been processed (configured with /tmp/positions.yaml or a persistent file).
  - **Scrape Target:**  
    Reads logs from /var/lib/docker/containers/*/*log.
  - **Pipeline Stages:**  
    - Parses JSON log entries.
    - Extracts labels (such as image_name and container_name) from the Docker logging tag formatted as {{.ImageName}}|{{.Name}}.
    - Uses start_position: end to only process new log entries, avoiding the ingestion of old logs.

### Grafana

- **Role:**  
  Grafana is used for log visualization and analysis. It provides a dashboard to explore logs stored in Loki.
- **Configuration Details:**
  - Auto-provisions Loki as a data source.
  - Runs on port **4000** (accessible via <http://localhost:4000>).
  - Offers query and visualization capabilities to monitor application performance and troubleshoot issues.

## Docker Compose Configuration

This Docker Compose file defines the entire logging stack, including your application containers (Python-app and Node-app), Loki, Promtail, and Grafana. It sets up a custom network named "loki" and configures each service with the necessary port mappings, volume mounts, and logging options. The logging options use the json-file driver with a custom tag format ({{.ImageName}}|{{.Name}}) to help Promtail extract labels efficiently.

```yaml

version: "3.3"

networks:
  loki:

services:
  Python-app:
    image: "em1999jay/python-app:latest"
    ports:
      - "5000:5000"
    logging:
      driver: "json-file"
      options:
        max-size: "100m"
        max-file: "10"
        tag: "{{.ImageName}}|{{.Name}}"

  Node-app:
    image: "em1999jay/moscow-time-app-node:v1"
    ports:
      - "3000:3000"
    logging:
      driver: "json-file"
      options:
        max-size: "100m"
        max-file: "10"
        tag: "{{.ImageName}}|{{.Name}}"

  loki:
    image: grafana/loki:latest
    ports:
      - "3100:3100"
    command: -config.file=/etc/loki/local-config.yaml
    networks:
      - loki
    logging:
      driver: "json-file"
      options:
        max-size: "100m"
        max-file: "10"
        tag: "{{.ImageName}}|{{.Name}}"

  promtail:
    image: grafana/promtail:latest
    volumes:
      - /var/log:/var/log
      - ./promtail.yml:/etc/promtail/config.yml:ro
      - /var/lib/docker/containers:/var/lib/docker/containers:ro
    command: -config.file=/etc/promtail/config.yml
    networks:
      - loki
    logging:
      driver: "json-file"
      options:
        max-size: "100m"
        max-file: "10"
        tag: "{{.ImageName}}|{{.Name}}"

  grafana:
    environment:
      - GF_PATHS_PROVISIONING=/etc/grafana/provisioning
      - GF_AUTH_ANONYMOUS_ENABLED=true
      - GF_AUTH_ANONYMOUS_ORG_ROLE=Admin
      - GF_FEATURE_TOGGLES_ENABLE=alertingSimplifiedRouting,alertingQueryAndExpressionsStepMode
    entrypoint:
      - sh
      - -euc
      - |
        mkdir -p /etc/grafana/provisioning/datasources
        cat <<EOF > /etc/grafana/provisioning/datasources/ds.yaml
        apiVersion: 1
        datasources:
        - name: Loki
          type: loki
          access: proxy
          orgId: 1
          url: http://loki:3100
          basicAuth: false
          isDefault: true
          version: 1
          editable: false
        EOF
        /run.sh
    image: grafana/grafana:latest
    ports:
      - "4000:3000"
    networks:
      - loki
    logging:
      driver: "json-file"
      options:
        max-size: "100m"
        max-file: "10"
        tag: "{{.ImageName}}|{{.Name}}"
```

---

## Promtail Configuration

This Promtail configuration file specifies how Promtail collects logs from Docker containers and forwards them to Loki. It sets up the server parameters and positions file, and defines the client endpoint for pushing logs to Loki. The scrape_configs section targets log files within Docker containers and includes pipeline stages to parse JSON log entries, extract relevant labels (such as image_name and container_name), and adjust timestamps.

```yaml

server:
  http_listen_port: 9080
  grpc_listen_port: 0

positions:
  filename: /tmp/positions.yaml
client:
  url: http://loki:3100/loki/api/v1/push
scrape_configs:
  - job_name: containers
    static_configs:
      - targets:
          - localhost
        labels:
          job: containerlogs
          __path__: /var/lib/docker/containers/*/*log  # For Linux systems only
    pipeline_stages:
      - json:
          expressions:
            stream: stream
            attrs: attrs
            tag: attrs.tag
            time: time
            log: log
      - timestamp:
          source: time
          format: RFC3339Nano
      - regex:
          expression: ^(?P<image_name>([^|]+))\|(?P<container_name>([^|]+))$
          source: "tag"
      - labels:
          stream:
          time:
          image_name:
          container_name:
          container_id:
```

### Application Containers

- **Role:**  
  These are the main application services that generate logs.
- **Configuration Details:**
  - **Python App:** em1999jay/python-app:latest
  - **Node App:** em1999jay/moscow-time-app-node:v1
  - Both are configured to use the json-file logging driver with a custom tag.
  
```sh
    tag: "{{.ImageName}}|{{.Name}}"  
```

- This tagging allows Promtail to extract meaningful labels while avoiding high cardinality.

### Bonus: Extra Application Integration

- **Role:**  
  An additional application has been integrated into the Docker Compose configuration to demonstrate comprehensive logging.
- **Configuration Details:**
  - The extra application is added as an independent service in docker-compose.yml.
  - Promtail is configured to scrape logs from all containers defined in the Compose file.
  - This ensures that every log, regardless of origin, is available for analysis in Grafana.

## Setup and Testing

### Directory Structure

```sh
S25-core-course-labss/  
├── monitoring/  
   ├── docker-compose.yml  
   ├── promtail.yml  
   ├── LOGGING.md
```

### Running the Stack

**Start the Stack:**  
   Navigate to the monitoring directory and run:  

```sh
   docker-compose up  
```

**Verify Component Operation:**

- **Loki:** Confirm that logs are being received on port **3100**.
  - **Promtail:** Check container logs to ensure that log scraping is occurring.
  - **Grafana:** Open your browser at <http://localhost:4000> to verify that the Loki data source is correctly configured and logs are visible.
  - **Extra Application:** Ensure that logs from the extra app are visible, demonstrating that the logging stack collects logs from every container.

### Screenshots

- **Container Logs:**  
  ![Container Logs](screenshots/containerlogs.png)
- **Grafana Logs:**  
  ![Grafana Logs](screenshots/grafanalogs.png)
- **Node App Logs:**  
  ![Node Logs](screenshots/nodelogs.png)
- **Promtail Logs:**  
  ![Promtail Logs](screenshots/promtaillogs.png)
- **Python App Logs:**  
  ![Python Logs](screenshots/pythonlogs.png)

## Conclusion

The logging stack successfully aggregates logs from multiple application containers (including the bonus extra application), processes them with Promtail, stores them in Loki, and provides visualization through Grafana.
