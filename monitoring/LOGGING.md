## Introduction

This report describes how the **Promtail**, **Loki**, and **Grafana** logging stack is configured and how it functions in our project. With this setup, logs from our **application containers** and the host system flow into **Loki**, where they can be queried and visualized in **Grafana**.

---

## Logging Stack Components

### 1. Promtail

**Promtail** is a lightweight log shipper that reads logs from specified paths or Docker containers and sends them to Loki. It:

- Monitors log files (e.g., `/var/log/*.log`) or container logs.
- Sends log data over HTTP to Loki (`http://loki:3100`).
- Uses a config file (e.g., `promtail-config.yml`) to define how logs are scraped and labeled.

### 2. Loki

**Loki** is a log aggregation system designed to be cost-effective and easy to scale:

- Receives logs from Promtail.
- Stores them in a compressed format (rather than a full-text index).
- Exposes a query API used by Grafana.
- Configured by `loki-config.yml` to handle chunk storage, indexing, etc.

### 3. Grafana

**Grafana** is the visualization layer:

- Connects to Loki as a data source.
- Lets you query logs in the **Explore** UI.
- Provides dashboards to combine metrics and logs in one interface.

---

## Docker Compose Setup

All three components can be run together in a single `docker-compose.yml` inside `monitoring/`. Below is an **example** snippet that also includes a sample `app_python` service:

```
version: "3.9"

networks:
  default:
    name: loki

services:

  app_python:
    image: billyboone/python-moscow-time:latest
    container_name: app_python
    ports:
      - "8080:5000"
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:5000"]
      interval: 10s
      timeout: 5s
      retries: 3
    logging:
      driver: json-file
      options:
        tag: app_python
        max-size: "10m"
        max-file: "10"

  loki:
    image: grafana/loki:2.9.2
    container_name: loki
    ports:
      - "3100:3100"
    command: -config.file=/etc/loki/local-config.yaml
    volumes:
      - ./loki-config.yml:/etc/loki/local-config.yaml:ro
    logging:
      driver: json-file
      options:
        tag: loki
        max-size: "10m"
        max-file: "10"

  promtail:
    image: grafana/promtail:2.9.2
    container_name: promtail
    volumes:
      - ./promtail.yml:/etc/promtail/config.yml:ro
      - /var/lib/docker/containers:/var/lib/docker/containers
    command: -config.file=/etc/promtail/config.yml
    depends_on:
      - loki
    logging:
      driver: json-file
      options:
        tag: promtail
        max-size: "10m"
        max-file: "10"

  grafana:
    image: grafana/grafana:latest
    container_name: grafana
    environment:
      - GF_PATHS_PROVISIONING=/etc/grafana/provisioning
      - GF_AUTH_ANONYMOUS_ENABLED=true
      - GF_AUTH_ANONYMOUS_ORG_ROLE=Admin
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
    ports:
      - "3000:3000"
    depends_on:
      - loki
    logging:
      driver: json-file
      options:
        tag: grafana
        max-size: "10m"
        max-file: "10"
```

### Logging Configuration

- **`logging.driver: json-file`** with `max-size` and `max-file` prevents logs from growing indefinitely.
- **Promtail** is set up to read container logs from `/var/lib/docker/containers`. Adjust your `promtail.yml` accordingly.

---

## System Architecture Diagram

```
[ app_python container logs ] => [ promtail ] -> [ loki ] -> [ grafana ]
```

---

## Screenshots

1. **Docker Compose Services\***Shows the running app_python, loki, promtail, and grafana containers.\*
2. **Grafana Explore\***Demonstrates log queries in Grafana’s Explore interface.\*

---

## Usage Instructions

1. **Place** `docker-compose.yml`, `promtail.yml`, and `loki-config.yml` in your `monitoring/` folder.
2. **Launch**:

   ```
   docker-compose up -d
   ```

3. **Access** Grafana at http://localhost:3000 → default creds `admin/admin`.
4. **Check** logs in **Grafana** → **Explore**, selecting **Loki** as the data source.
5. **Optional**: Confirm `app_python` is responding at [http://localhost:8080](http://localhost:8080/).

---
