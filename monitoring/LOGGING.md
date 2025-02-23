## Logging Overview
# The logging consists of Loki, Promtail, and Grafana, working together for collecting, storing, and visualizing logs.

`Loki`: A log aggregation system for storing log data efficiently.
`Promtail`: A log forwarder for collecting logs from local sources and sending them to the Loki.
`Grafana`: A visualization tool that allows querying and analyzing logs stored in the Loki.

## How It Works

1) `Applications Logs`:
- `app-python` and `app-go` services will generate logs.

2) `Promtail Collecting Logs`:
- Promtail reads logs from /var/lib/docker/containers/*/*log.
- The logs are labeled and forwarded to the Loki.

3) `Loki Storing Logs`:
- Loki indexes the logs efficiently.

4) `Grafana Displaying Logs`:
- Grafana queries Loki and visualizes logs for monitoring.

# Starting with `docker-compose up -d`:
![alt text](image.png)

# Main page Grafana:
![alt text](image-1.png)

# Loki connection:
![alt text](image-2.png)

# Test log from console:
![alt text](image-3.png)
