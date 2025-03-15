# Logging Stack Documentation

## Overview

This document describes the logging stack implementation using Grafana, Loki, and Promtail. The stack is designed to collect, store, and visualize logs from our Docker containers and system services.

## Components

### 1. Loki
- **Role**: Log aggregation system that stores and indexes logs
- **Port**: 3100
- **Configuration**: Uses local file system storage with BoltDB indexing
- **Key Features**:
  - Stores logs efficiently
  - Provides fast queries
  - Integrates seamlessly with Grafana
  - Uses labels for efficient log organization

### 2. Promtail
- **Role**: Log collector that ships logs to Loki
- **Port**: 9080
- **Key Features**:
  - Discovers targets
  - Attaches labels to log streams
  - Pushes logs to Loki
- **Configured Sources**:
  - Docker container logs
  - System logs

### 3. Grafana
- **Role**: Visualization platform for logs
- **Port**: 3000
- **Features**:
  - Web interface for log querying
  - Dashboard creation
  - Alert configuration
  - Anonymous access enabled for easy testing

### 4. Application Container
- Configured with json-file logging driver
- Log rotation enabled:
  - Maximum file size: 10MB
  - Maximum number of files: 3

## Setup Instructions

1. Create the following directory structure:
```
monitoring/
├── docker-compose.yml
├──loki-config.yaml
└── promtail.yml
```


2. Start the stack:
```bash
cd monitoring
docker-compose up -d
```

3. Access Grafana:
- Open http://localhost:3002 in browser
- Navigate to Configuration → Data Sources
- Add Loki (http://loki:3100) as a data source

## Querying Logs

1. In Grafana, go to Explore
2. Select Loki as the data source
3. Use LogQL to query logs, for example:
   - `{job="docker"}` - shows all Docker container logs
   - `{job="system"}` - shows system logs

## Maintenance

- Log files are automatically rotated when they reach 10MB
- A maximum of 3 log files are kept per container
- Loki stores indexes and chunks in the local filesystem
- Monitor disk usage of the logging stack periodically

## Troubleshooting

1. If logs are not appearing:
   - Check Promtail status: `docker-compose logs promtail`
   - Verify Loki is receiving data: `docker-compose logs loki`
   - Ensure proper permissions on Docker log directory

2. If Grafana can't connect to Loki:
   - Verify Loki is running: `docker-compose ps`
   - Check Loki is accessible: `curl http://localhost:3100/ready`
   - Review Grafana data source configuration