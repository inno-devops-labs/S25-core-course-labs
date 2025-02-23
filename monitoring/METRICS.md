### **1. Prometheus overview**
Prometheus is an open-source monitoring solution that collects and stores time-series metrics. Key concepts include:
- **Metrics & labels**: Metrics are uniquely identified using names and labels.
- **Scrape targets**: Prometheus pulls data from services using HTTP.
- **PromQL**: A query language used for retrieving and visualizing metrics.

### **2. Prometheus in Docker Compose**
Prometheus has been added to `docker-compose.yml` with:
- Port mapping on `9090`
- Persistent volume mounting
- Health check for availability

### **3. Prometheus configuration**
Prometheus scrapes data from:
- Itself (`localhost:9090`)
- Loki (`loki:3100`)
- Application (`app:5000`)

---

### **1. Grafana dashboards**
- Imported dashboards for:
  - [Loki](https://grafana.com/grafana/dashboards/13407)
  - [Prometheus](https://grafana.com/grafana/dashboards/3662)
- Configured data sources in Grafana to use Prometheus.

### **2. Service enhancements**
**Enhancements made to `docker-compose.yml`:**
- **Log rotation** added:
  ```yaml
  logging:
    driver: "json-file"
    options:
      max-size: "10m"
      max-file: "3"
    ```
- **Memory limits**
```deploy:
  resources:
    limits:
      memory: 500M```
