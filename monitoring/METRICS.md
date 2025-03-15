## Metrics
- I used bashboards provided as references.
- Loki and Prometheus have endpoint to expose metrics, so I collect this metrics using Prometheus.
- After that I create dashboard from template for both services.
- After all I add logging rotation settings in docker-compose file:
    - max logs files number is 3
    - max log file size is 15 MB
- As the last step resource restrictions were added in docker-compose file:
    - max memory usage is 512 MB per service


## Screenshots
- prometheus targets
![prometheus](/monitoring/screenshots/prometheus.png)
- uptime for prometheus
![prometheus](/monitoring/screenshots/prometheus-uptime.png)
- uptime for loki
![prometheus](/monitoring/screenshots/loki-uptime.png)
- loki dashboard
![loki1](/monitoring/screenshots/loki-dashboard.png)
- prometheus dashboards
![prometheus1](/monitoring/screenshots/prometheus-dashboard-1.png)
![prometheus2](/monitoring/screenshots/prometheus-dashboard-2.png)