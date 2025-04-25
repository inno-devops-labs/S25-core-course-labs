# Lab 8: Monitoring with Prometheus
## Task 1: Prometheus Setup
```txt
fridorovich@DESKTOP-FRR2QTC:/home/devops/S25-core-course-labs/monitoring$ docker ps
CONTAINER ID   IMAGE                                 COMMAND                  CREATED          STATUS                             PORTS
                                                                                     NAMES
48932c723d4d   grafana/loki:latest                   "/usr/bin/loki -conf…"   41 seconds ago   Up 40 seconds                      0.0.0.0:3100->3100/tcp, [::]:3100->3100/tcp       
                                                                                     monitoring-loki-1
4cb7468e2bff   prom/prometheus:latest                "/bin/prometheus --c…"   41 seconds ago   Up 40 seconds                      0.0.0.0:9090->9090/tcp, [::]:9090->9090/tcp       
                                                                                     monitoring-prometheus-1
81ea6d953233   fridorovich04/app_python:latest       "uvicorn main:app --…"   41 seconds ago   Up 40 seconds (health: starting)   0.0.0.0:8000->80/tcp, [::]:8000->80/tcp
                                                                                     monitoring-app_python-1
ec66725c3fca   grafana/grafana:latest                "/run.sh"                41 seconds ago   Up 40 seconds                      0.0.0.0:3000->3000/tcp, [::]:3000->3000/tcp       
                                                                                     monitoring-grafana-1
2f28b2c78650   grafana/promtail:latest               "/usr/bin/promtail -…"   41 seconds ago   Up 40 seconds
                                                                                     monitoring-promtail-1
```
![](prom.png)
