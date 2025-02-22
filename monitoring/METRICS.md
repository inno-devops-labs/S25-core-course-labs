# Prometheus and Grafana Monitoring Setup

### Task 1: Prometheus Setup

1. **Prometheus Integration**
   - Added Prometheus service to `docker-compose.yml`.
   - Configured log rotation (`max-size: 10m`, `max-file: 3`) and memory limits (512MB).

2. **Prometheus Configuration**
   - Configured `prometheus.yml` to scrape metrics from Prometheus, Loki, Promtail, Grafana, and application services.

3. **Verification**
   - Verified Prometheus targets via `http://localhost:9090/targets`.

![alt text](https://github.com/DoryShibkova/S25-core-course-labs/blob/lab8/monitoring/ScreensMetrics/%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82%2019-02-2025%20154739.jpg)

---

### Task 2: Dashboard and Configuration Enhancements

1. **Grafana Dashboards**
   - Configured dashboards for Loki and Prometheus.
   - Added Loki and Prometheus as data sources.

2. **Service Configuration**
   - Updated `docker-compose.yml` with log rotation and memory limits for all services.

3. **Metrics Gathering**
   - Extended Prometheus configuration to scrape metrics from all services.

![alt text](https://github.com/DoryShibkova/S25-core-course-labs/blob/lab8/monitoring/ScreensMetrics/%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82%2019-02-2025%20155903.jpg)
![alt text](https://github.com/DoryShibkova/S25-core-course-labs/blob/lab8/monitoring/ScreensMetrics/%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82%2019-02-2025%20173617.jpg)
![alt text](https://github.com/DoryShibkova/S25-core-course-labs/blob/lab8/monitoring/ScreensMetrics/%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82%2019-02-2025%20233925.jpg)
![alt text](https://github.com/DoryShibkova/S25-core-course-labs/blob/lab8/monitoring/ScreensMetrics/%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82%2019-02-2025%20233949.jpg)
![alt text](https://github.com/DoryShibkova/S25-core-course-labs/blob/lab8/monitoring/ScreensMetrics/%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82%2019-02-2025%20234415.jpg)
![alt text](https://github.com/DoryShibkova/S25-core-course-labs/blob/lab8/monitoring/ScreensMetrics/%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82%2019-02-2025%20234445.jpg)
![alt text](https://github.com/DoryShibkova/S25-core-course-labs/blob/lab8/monitoring/ScreensMetrics/%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82%2019-02-2025%20234708.jpg)

# Application Metrics & Health Checks

## 1. Application Metrics
- Integrated Prometheus client in the `app-python` service.
- Exposed metrics on port `8001`.
- Metrics visible at: `http://localhost:8001/metrics`

## 2. Health Checks
- Added Docker health checks for `app-python`:
  - Endpoint: `http://localhost:8000`
  - Interval: 30s, Timeout: 5s, Retries: 3

![alt text](https://github.com/DoryShibkova/S25-core-course-labs/blob/lab8/monitoring/bonusImg/img5.jpg)
![alt text](https://github.com/DoryShibkova/S25-core-course-labs/blob/lab8/monitoring/bonusImg/img1.jpg)
![alt text](https://github.com/DoryShibkova/S25-core-course-labs/blob/lab8/monitoring/bonusImg/img2.jpg)
![alt text](https://github.com/DoryShibkova/S25-core-course-labs/blob/lab8/monitoring/bonusImg/img3.jpg)
![alt text](https://github.com/DoryShibkova/S25-core-course-labs/blob/lab8/monitoring/bonusImg/img4.jpg)
