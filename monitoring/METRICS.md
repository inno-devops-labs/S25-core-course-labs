# Monitoring with Prometheus

![prom.png](prometheus.png)
**Import Loki dashboard**
![Loki_import.png](Loki/Loki_import.png)

**Loki dashboard**
![Loki_import.png](Loki/1.png)
![Loki_import.png](Loki/2.png)
![Loki_import.png](Loki/3.png)

**Import prometheus dashboard**
![import_dashboard.png](prometheus/import_dashboard.png)

**Prometheus dashboard**
![import_dashboard.png](prometheus/1.png)
![import_dashboard.png](prometheus/2.png)
![import_dashboard.png](prometheus/3.png)
![import_dashboard.png](prometheus/4.png)
![import_dashboard.png](prometheus/5.png)

## Log rotation and Memory limits 
```
    deploy:
      resources:
        limits:
          memory: 200M
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
```