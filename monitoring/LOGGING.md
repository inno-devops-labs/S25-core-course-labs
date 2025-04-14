# Logging

## Overview

In general all I did was taking the provided examples for [docker-compose](https://github.com/grafana/loki/blob/main/production/docker-compose.yaml) and [promtail configuration](https://github.com/black-rosary/loki-nginx/blob/master/promtail/promtail.yml), and adapth them for my needs. For `docker-compose` I only added my containers and did some minor adjustments. In case of protail config, I did more significant changes and simplifications. Then I just booted everything up and explored how this works.

## Components

### 1. Loki

**Role:** Log aggregation and storage.

- **Image:** grafana/loki:2.9.2
- **Port:** 3100
- **Configuration:** `/etc/loki/local-config.yaml`
- **Purpose:** Loki is a log aggregation system that indexes and stores logs. It is optimized for high performance and low resource consumption by indexing metadata rather than the raw log content.

### 2. Promtail

**Role:** Log collection and forwarding.

- **Image:** grafana/promtail:2.9.2
- **Configuration:** `/etc/promtail/config.yml`
- **Volumes:**
  - `/var/lib/docker/containers:/var/lib/docker/containers` – Access to container logs.
- **Purpose:** Promtail is a log shipper that tails log files and forwards them to Loki. It reads logs from Docker container log files and attaches metadata such as container ID, image name, and container name.

#### Key Configurations (promtail-config.yaml)

- **Server:**
  - HTTP listening port: `9080`
  - gRPC listening port: Disabled
  - Log level: `warn`
- **Positions:**
  - State file for tracking read positions: `/var/lib/promtail/positions/positions.yaml`
- **Client:**
  - Loki push endpoint: `http://loki:3100/api/prom/push`
- **Scrape Configs:**
  - `job_name: docker` – Collects logs from Docker containers.
  - `static_configs` – Reads logs from `/var/lib/docker/containers/*/*log`.
  - **Pipeline Stages:**
    - `json` – Extracts fields like `stream`, `tag`, and `time` from JSON log lines.
    - `regex` – Extracts `container_id` from the log file path.
    - `timestamp` – Parses `time` field as RFC3339Nano timestamp.
    - `labels` – Assigns extracted fields as labels for querying in Loki.
    - `output` – Specifies the `log` field as the final message content.

### 3. Grafana

**Role:** Log visualization and dashboarding.

- **Image:** grafana/grafana:latest
- **Port:** 3000
- **Provisioning:** Configures Loki as a default data source using the `GF_PATHS_PROVISIONING` environment variable and an inline `ds.yaml` configuration.
- **Purpose:** Grafana visualizes logs and metrics, enabling powerful querying and dashboard creation. It connects to Loki for log visualization.

### 4. Application Containers

**moscow-time-app:**

- A Python application exposing an HTTP endpoint on port `8081`.

**url_shortener:**

- A Go application exposing an HTTP endpoint on port `8080`.
- Configured with `config/local.yaml` during build.

These containers generate logs that Promtail collects and forwards to Loki for aggregation.

## Network Configuration

All services are connected to a custom Docker network named `loki` to facilitate inter-service communication.

## Data Flow Summary

1. Application containers generate logs (stdout/stderr), saved in `/var/lib/docker/containers/<container_id>/<container_id>-json.log`.
2. Promtail reads and processes log files, extracting metadata and formatting timestamps.
3. Logs are pushed to Loki with labels such as `container_id`, `stream`, and `image_name`.
4. Grafana queries Loki for logs and presents them in a user-friendly interface.

## Accessing the Stack

- **Grafana UI:** <http://localhost:3000>
- **Loki API:** <http://localhost:3100>

## Screenshots

### Moscow Time App

![moscow-time-app](/monitoring/media/time.png)

### Url Shortener

![url-shortener](/monitoring/media/url.png)

### Grafana

![url-shortener](/monitoring/media/grafana.png)

### Loki

![url-shortener](/monitoring/media/loki.png)

### Promtail

![url-shortener](/monitoring/media/promtail.png)
