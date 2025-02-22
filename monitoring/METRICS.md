### Task 1:
- Ensuring that Prometheus is correctly scraping metrics:
  - 1. **Both targets are up:** ![alt text](image-8.png)
  - 2. **Checking prometheus with query:** ![alt text](image-5.png)
  - 3. **Checking loki with query:** ![alt text](image-6.png)

---

### Task 2 Dashboards:
- Set up dashboards in Grafana
  - 1. **For loki:** ![alt text](image-7.png)
  - 2. **For prometheus:** ![alt text](image-9.png)

---

### Task 2 Service Configuration Updates:
- Enhanced the configuration of all services in `docker-compose.yml`:
  - **Added log rotation mechanisms:**
    - Implemented `json-file` driver with `max-size: 30m` and `max-file: 3`.
  - **Specified memory limits for containers:**
    - `app-python`: `500m`
    - `app-go`: `500m`
    - `loki`: `1g`
    - `alloy`: `500m`
    - `grafana`: `1g`
    - `prometheus`: `500m`
  - **CPU limits set for better resource management:**
    - `app-python`: `0.5`
    - `app-go`: `0.5`
    - `loki`: `0.5`
    - `alloy`: `0.3`
    - `grafana`: `0.5`
    - `prometheus`: `0.3`

