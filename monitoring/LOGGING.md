# Logging Overview

## Grafana
Grafana is a tool for visualizing data from various sources. Here, it is used to view and search logs stored in Loki. It is set up as the default data source.

Grafana Setup

## Loki
Loki is a lightweight log storage system. It stores application logs, indexes them by labels, and enables fast searches.

## Promtail
Promtail collects logs from specified sources and sends them to Loki. Since the applications do not use specific log files, Promtail gathers logs from all running Docker containers.

## Applications
The Kotlin Ktor and Python Flask applications log messages to STDOUT, which are then captured by Promtail. While the logs are not fully structured, Loki can still detect some details, such as the LOG LEVEL from the Python app.

## Logs

### Python
- [Python1](logs/py_log1.png)
- [Python2](logs/py_log2.png)
- [Python3](logs/py_log3.png)
- [Kotlin1](logs/kotlin_log1.png)
- [Kotlin2](logs/kotlin_log2.png)
- [Kotlin3](logs/kotlin_log3.png)
