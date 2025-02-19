# Logging Stack Setup

## Components

- **Loki:** Collects logs and stores them.
- **Promtail:** Reads logs from Docker containers and forwards them to Loki.
- **Grafana:** Provides a dashboard to visualize logs.

## Configuration

- docker-compose.yml defines the services.
- promtail.yml configures log scraping.

## Testing Steps

1. Verify Loki: curl http://localhost:3100/ready
2. Verify Promtail: docker logs monitoring-promtail-1
3. Access Grafana: http://localhost:3000/ (default login: admin/admin)

## Screenshots


