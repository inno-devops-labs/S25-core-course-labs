# Logging.md 

## Roles of stack components 

### Loki
Loki is a log aggregation system designed to store and query logs. It is optimized for storing logs in a highly efficient manner, allowing for fast retrieval and analysis. Loki integrates seamlessly with Grafana, enabling users to visualize logs alongside metrics.

### Promtail
Promtail is an agent that collects logs from various sources and forwards them to Loki. It is responsible for scraping logs from files, such as `app.log`, and can be configured to parse and label logs before sending them to Loki. Promtail acts as the bridge between your application logs and the Loki backend.

### Grafana
Grafana is a visualization tool that allows users to create dashboards and alerts based on data from various sources, including Loki. In the context of logging, Grafana provides a user-friendly interface to query, visualize, and analyze logs stored in Loki. It supports creating alerts based on log patterns and metrics.

## What did I change in my app

To add logging to my application, I created `logging_config.py` with settings for the Python logger. It saves logs in a plain text file named `app.log`.

The log format is `%(asctime)s - %(name)s - %(levelname)s - %(message)s`, where the messages in my case are `Received request: {request.method} {request.url}`.

## Screenshots 
![Screenshot 1](screenshots/img1.png)
![Screenshot 2](screenshots/img2.png)
![Screenshot 3](screenshots/img3.png)

## Improve points 

* Log more actions in the application (errors, accesses, session time)
* Log system processes as well
* Create labels to simplify interaction with logs
* Create metrics and alerts in Grafana
