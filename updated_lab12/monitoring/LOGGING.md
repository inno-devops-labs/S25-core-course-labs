# Logging Stack with Loki, Promtail, and Grafana

## Architecture  
![Loki Stack Architecture](screenshots/loki_architecture_components.svg)  
*Components: Loki (storage), Promtail (log collection), Grafana (visualization).*

---

## **Components & Services**  
### 1. **Loki**  
- **Role**: Log aggregation and storage.  
- **Access**: `http://localhost:3100`  
- **Config**: Uses `loki-config.yaml` for single-node setup.  

### 2. **Promtail**  
- **Role**: Collects logs from Docker containers.  
- **Key Features**:  
  - Auto-discovers containers via Docker socket.  
  - Adds labels: `container`, `logpath`, `job="docker"`.  

### 3. **Grafana**  
- **Role**: Visualize and query logs.  
- **Access**: `http://localhost:3000` (admin/admin).  

### 4. **Applications**  
- **`myapp`**: Custom application (e.g., `yehiasobeh/moscow-time-app`).  
- **`extra-app`**: Bonus service (e.g., NGINX).  

---

## **Setup Steps**  
1. **Start the Stack**:  
   ```bash
   docker-compose up -d
   ```

2. **Verify Running Services**:
   ```bash
   docker ps
   ```

---

## **Log Query Examples**  
### 1. All Docker Logs  
   ```logql
   {job="docker"}
   ```

### 2. Filter by Container  
   ```logql
   {container="monitoring_myapp_1"}
   ```
   *Replace `monitoring_myapp_1` with your container name.*  


### 3. Filter by Service  
   ```logql
   {job="docker"} |= "GET"
   ```

---

## **Screenshots**  
### 1. Grafana Data Source  
*Loki configured with URL `http://loki:3100`.*  
![](/screenshots/loki1.png)
![](/screenshots/loki2.png)
![](/screenshots/loki3.png)


### 2. Logs Filtered by Container  
*Query: `{container="monitoring_myapp_1"}`.*  
   ![](/screenshots/myapp.png)

### 3. Bonus Application Logs  
*Logs from `extra-app` (NGINX).*  
   ![](/screenshots/extra.png)

---

## Key Labels
| Label           | Source                  | Example Value                |
|-----------------|-------------------------|------------------------------|
| `container`     | Docker container name   | `monitoring_myapp_1`         |
| `service_name`  | Docker Compose service  | `myapp`, `extra-app`         |


---

## **Troubleshooting**  
### Missing Labels?  
Verify Promtail’s Docker socket access:  
```bash
docker exec monitoring_promtail_1 ls /var/run/docker.sock
```

Check Promtail logs:  
```bash
docker logs monitoring_promtail_1
```



---

## **Bonus Task**  
**Extra Service Added**: NGINX (`extra-app`).  

**Log Query**:  
```logql
{container="monitoring_extra-app_1"}
