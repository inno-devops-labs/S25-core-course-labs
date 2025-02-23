# Metrics Monitoring Report (Lab 8)

## Task 1: Prometheus Configuration
### Implemented Features
1. Added Prometheus service to `docker-compose.yml`
2. Configured scraping targets for:
   - Loki metrics endpoint (`loki:3100`)
   - Application metrics endpoint (`app:8000`)
   - Self-monitoring (`localhost:9090`)

### Verification
```bash
# Check active targets (all should show 'HEALTHY')
curl http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | .scrapePool + ": " + .health'

