# Logging Stack Report

## This md file provides an overview of the logging stack setup using Loki, Promtail and Grafana

## Components

### 1. Loki

- Loki is a log aggregation system designed for storing and querying logs efficiently
- It is optimized for **scalability** and integrates well with Grafana
- Configuration file: loki-config.yml
- Runs on port 3100

### 2. Promtail

- Promtail is responsible for collecting logs and sending them to Loki
- It reads logs from `/var/log/*.log` and labels them for querying in Grafana
- Configuration file: promtail-config.yml

### 3. Grafana

- Grafana provides a web-based UI to visualize logs
- It connects to Loki as a **data source**
- Accessible at `http://localhost:3000` (default credentials: **admin/admin**)

## Setup Instructions

### to start this logging stack, run the following command inside monitoring dir: **docker-compose up -d**
