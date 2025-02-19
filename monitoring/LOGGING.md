# Logging Stack Setup

## Components

- **Loki:** Collects logs and stores them.
- **Promtail:** Reads logs from Docker containers and forwards them to Loki.
- **Grafana:** Provides a dashboard to visualize logs.

## Configuration

- docker-compose.yml defines the services.
- promtail.yml configures log scraping.

## Testing Steps

1. Verify Loki: curl http://localhost:3100/ready
2. Verify Promtail: docker logs monitoring-promtail-1
3. Access Grafana: http://localhost:3000/ (default login: admin/admin)

## Screenshots

#### Loki Logs
![alt text](https://github.com/DoryShibkova/S25-core-course-labs/blob/lab7/monitoring/%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82%2018-02-2025%20161108.jpg)


#### Promtail Logs
![alt text](https://github.com/DoryShibkova/S25-core-course-labs/blob/lab7/monitoring/%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82%2018-02-2025%20161239.jpg)


#### Grafana Logs
![alt text](https://github.com/DoryShibkova/S25-core-course-labs/blob/lab7/monitoring/%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82%2018-02-2025%20161331.jpg)
![alt text](https://github.com/DoryShibkova/S25-core-course-labs/blob/lab7/monitoring/%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82%2018-02-2025%20161401.jpg)
![alt text](https://github.com/DoryShibkova/S25-core-course-labs/blob/lab7/monitoring/%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82%2018-02-2025%20161433.jpg)



### docker-compose logs -f
![alt text](https://github.com/DoryShibkova/S25-core-course-labs/blob/lab7/monitoring/%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82%2018-02-2025%20161648.jpg)
![alt text](https://github.com/DoryShibkova/S25-core-course-labs/blob/lab7/monitoring/%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82%2018-02-2025%20161704.jpg)
![alt text](https://github.com/DoryShibkova/S25-core-course-labs/blob/lab7/monitoring/%D0%A1%D0%BA%D1%80%D0%B8%D0%BD%D1%88%D0%BE%D1%82%2018-02-2025%20161951.jpg)
