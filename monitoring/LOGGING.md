# Logging

## Components
### Promtail
It is log shipper agent that reads, enrich adn send to data to a log aggregator such as Loki. My implementaion collect all docker container logs and add job label.

### Loki
Loki is a log aggregator backend that collect logs, index it to fast seaching log data. Also provides decriptive language LogQL to query data

### Grafana
Visualization tool

## Screenshots
![grafana](/monitoring//screenshots/grafana.png)