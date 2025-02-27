# Logging Stack

This directory contains a Docker Compose configuration for setting up a complete logging stack consisting of:

- **Loki** - Log aggregation system
- **Promtail** - Log collection agent
- **Grafana** - Visualization platform
- **Flask Python App** - A Python Flask application that logs to files
- **Demo App** - Sample NGINX application for log generation

## Usage

To start the logging stack:

```bash
docker-compose up -d
```

To stop the logging stack:

```bash
docker-compose down
```

## Access Services

Once running, you can access:

- **Grafana**: http://localhost:3000
- **Loki API**: http://localhost:3100
- **Python Flask App**: http://localhost:5001
- **Demo App (NGINX)**: http://localhost:8080

## Log Queries

Grafana is pre-configured with a Loki data source and sample dashboards. You can also run custom queries using LogQL:

- Basic query: `{job="nginx"}`
- Filter by status code: `{job="nginx"} |= "404"`
- Count status codes: `count_over_time({job="nginx"}[1m])`
- Python app logs: `{job="python_app"}`
- Python app errors: `{job="python_app"} |= "ERROR"`

## Dashboards

The logging stack comes with pre-configured dashboards:

1. **Log Dashboard** - Shows general logs from NGINX and Docker
2. **Python Application Dashboard** - Specifically for monitoring the Python Flask application

## Troubleshooting

- If logs are not appearing, check Promtail's status by looking at its logs: `docker-compose logs promtail`
- To check if Loki is receiving logs: `curl http://localhost:3100/ready`
- To verify Python app logging is working: `docker-compose logs python-app`

## Python App Integration

The Python Flask app has been configured to:

1. Write logs to `/home/appuser/logs/app.log`
2. Use a shared volume that Promtail can access
3. Log various events including:
   - Page access
   - Health checks
   - 404 and 500 errors 