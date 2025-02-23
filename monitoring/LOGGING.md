# Logging Stack Documentation

## Components
- **Loki**: Log storage and indexing system (like a search engine for logs)
- **Promtail**: Log collector that scrapes container logs and sends to Loki
- **Grafana**: Visualization platform for exploring and analyzing logs

## Setup Guide
1. **Start the stack**:
   ```bash
   docker-compose -f monitoring/docker-compose.yml up -d
   
2. **Access Grafana:**
Open http://localhost:3000 in your browser
Use credentials:
```bash
Login: admin
Password: admin
```

3. **Configure Loki datasource**:
* Go to Explore section 
* Select "Loki" from datasource dropdown

## Querying Logs
Find your application logs using:
```logql
{container="monitoring_app_1"}
```

