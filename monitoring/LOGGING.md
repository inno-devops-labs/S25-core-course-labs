# Lab 7: Monitoring and Logging

## Main information
This lab inclued process of setting up a logging stack using Promtail, Loki, and Grafana. The main goal is to configure a Docker Compose setup that integrates logging with my python and js applications.

The configuration is defined in a Docker Compose file that deploys the following services:
- **Loki:** Aggregates and indexes logs.
- **Promtail:** Collects logs from Docker and application volumes, then pushes them to Loki.
- **Grafana:** Visualizes logs via a provisioned Loki data source.
- **Application Services:** 
  - **app_python:** A distroless Python application that show Moscow time.
  - **app_node:** A distroless Node.js application that shows quotes that are connected with programming. 
- **Volumes:** Dedicated volumes for persistent storage of logs and Grafana data.

![](/monitoring/images/dockers.png)

---

## Logging Stack Setup 

### 1. Create a Monitoring Folder
Create a folder named `monitoring` in your project directory:
```sh
mkdir monitoring
cd monitoring
```

### 2. Docker Compose Configuration
Create a `docker-compose.yml` file in the `monitoring` folder with the following content:

#### **docker-compose.yml:**
```yaml
version: '3.8'

networks:
  loki:

services:
  loki:
    image: grafana/loki:latest
    ports:
      - "3100:3100"
    command: -config.file=/etc/loki/local-config.yaml
    volumes:
      - ./loki-config.yml:/etc/loki/loki-config.yaml
      - loki-storage:/tmp/loki
    networks:
      - loki

  promtail:
    image: grafana/promtail:latest
    volumes:
      - /var/log:/var/log
      - ./promtail.yml:/etc/promtail/config.yml
      - /var/lib/docker/containers:/var/lib/docker/containers:ro
      - app_logs:/app_logs:ro
    command: -config.file=/etc/promtail/config.yml
    networks:
      - loki

  grafana:
    environment:
      - GF_PATHS_PROVISIONING=/etc/grafana/provisioning
      - GF_AUTH_ANONYMOUS_ENABLED=true
      - GF_AUTH_ANONYMOUS_ORG_ROLE=Admin
      - GF_FEATURE_TOGGLES_ENABLE=alertingSimplifiedRouting,alertingQueryAndExpressionsStepMode
    entrypoint:
      - sh
      - -euc
      - |
        mkdir -p /etc/grafana/provisioning/datasources
        cat <<EOF > /etc/grafana/provisioning/datasources/ds.yaml
        apiVersion: 1
        datasources:
        - name: Loki
          type: loki
          access: proxy 
          orgId: 1
          url: http://loki:3100
          basicAuth: false
          isDefault: true
          version: 1
          editable: false
        EOF
        /run.sh
    image: grafana/grafana:latest
    ports:
      - "3000:3000"
    volumes:
      - grafana-storage:/var/lib/grafana
    networks:
      - loki

  app_python:
    image: twentythree3/moscow-time-app-distroless:latest
    ports:
      - "5001:5001"
    volumes:
      - app_logs:/app/logs
    networks:
      - loki

  app_node:
    image: twentythree3/my-node-app-distroless:latest
    ports:
      - "3001:3001"
    volumes:
      - app_logs:/app/logs
    networks:
      - loki

volumes:
  grafana-storage:
  loki-storage:
  app_logs:
    driver: local
```

Explanation:

Networks & Volumes:
    
    All services share the loki network. Volumes are defined for persistent storage of Loki data, Grafana data, and application logs.

Service Configurations:
    
    Each service mounts its configuration file and required volumes.

### 3. Loki

Create Loki-config.yml by command:
```shell
wget https://raw.githubusercontent.com/grafana/loki/v3.0.0/cmd/loki/loki-local-config.yaml -O loki-config.yml
```

### 4. Loki-config Configuration

This file configures Loki's server settings, storage, and query parameters:

```yml
auth_enabled: false

server:
  http_listen_port: 3100
  grpc_listen_port: 9096

common:
  instance_addr: 127.0.0.1
  path_prefix: /tmp/loki
  storage_config:
    filesystem:
      chunks_directory: /tmp/loki/chunks
      rules_directory: /tmp/loki/rules
  replication_factor: 1
  ring:
    kvstore:
      store: inmemory

query_range:
  results_cache:
    cache:
      embedded_cache:
        enabled: true
        max_size_mb: 100

schema_config:
  configs:
    - from: 2020-10-24
      store: tsdb
      object_store: filesystem
      schema: v12
      index:
        prefix: index_
        period: 24h
```


### 4. Promtail 
Create `promtail.yml` by command:

```shell
wget https://raw.githubusercontent.com/grafana/loki/v3.0.0/clients/cmd/promtail/promtail-docker-config.yaml -O promtail.yml
```

### 5. Promtail configuration 
Then edit promtail to have logs from docker and apps.

The promtail.yml says Promtail which logs to scrape and where to send them:
#### **promtail.yml:**
```yaml
server:
  http_listen_port: 9080
  grpc_listen_port: 0

positions:
  filename: /tmp/positions.yaml

client:
  url: http://loki:3100/api/prom/push

scrape_configs:
  - job_name: docker_logs
    static_configs:
      - targets:
          - localhost
        labels:
          job: docker
          __path__: /var/lib/docker/containers/*/*log

  - job_name: python_app_logs
    static_configs:
      - targets: [ "localhost" ]
        labels:
          job: python_app
          __path__: /app_logs/app_python.log

  - job_name: node_app_logs
    static_configs:
      - targets: [ "localhost" ]
        labels:
          job: node_app
          __path__: /app_logs/app_nodejs.log
```
Scrape Jobs:

    Promtail is set to scrape logs from Docker containers as well as from the application log files stored in /app_logs.

Client Section:

    Logs are pushed to Loki via http://loki:3100/api/prom/push.

### 6. Testing
Run the stack:
```sh
docker-compose up -d
```



# Reporting

How the Stack Works:

Log Generation:
        
        Docker Containers generate logs using the JSON-file logging driver. Applications write logs to a shared volume (app_logs), which is mounted into the containers.

Log Collection:
        
        Promtail scrapes logs from both Docker container directories and the custom /app_logs directory.

Log Aggregation:
        
        Loki receives logs from Promtail, indexes them, and stores them for later querying.

Log Visualization:
        
        Grafana connects to Loki and provides dashboards to query and visualize log data.

## Screenshots
- All logs from Docker

![](/monitoring/images/dockerlogs.png)

![](/monitoring/images/dockerlogss.png)
- Logs from python app

![](/monitoring/images/pythonapp.png)

- Logs from node app

![](/monitoring/images/appnode.png)





