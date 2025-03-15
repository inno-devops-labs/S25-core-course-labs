# Monitoring with Prometheus

With Prometheus successfully set up and scraping metrics from Loki, Grafana, and the Flask application, we now have a robust monitoring system in place.

## Prometheus Configuration

Prometheus is configured with the following settings:

- **Scrape interval**: 15 seconds
- **Evaluation interval**: 15 seconds
- **Monitored Services**:
  - `Prometheus` (`localhost:9090`)
  - `loki` (`loki:3100`)
  - **Flask application (app_python)** (`localhost:5000/metrics`)
  - `Grafana` (`localhost:3000`)

## Accessing Prometheus

To verify that Prometheus is running and collecting metrics:

1. Open a web browser and navigate to:

   - `http://localhost:9090`

2. Click on **Status -> Targets** or visit:

   - `http://localhost:9090/targets`

3. Ensure all configured targets are listed and in an **UP** state.

#### Prometheus Targets Page

Shows all active targets being scraped

![Screenshot_33.jpg](Data%20for%20report/Screenshot_33.jpg)

## Troubleshooting

#### Prometheus Not Running

- Check logs using:

  ```bash
  sudo docker-compose logs prometheus
  ```
  
- Ensure `docker-compose.yml` includes the Prometheus service.

#### Targets Showing as DOWN

- Verify that the services are running:

  ```bash
  sudo docker ps
  ```
  
- Check connectivity using:

  ```bash
  curl http://localhost:<PORT>/metrics
  ```
  
(To the folder **Data for report** I have attached some logs that I saved while working in **PyCharm**)