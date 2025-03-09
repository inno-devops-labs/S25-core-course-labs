# Monitoring and Logging

This logging stack efficiently collects, stores, and visualizes logs for better observability and debugging. By leveraging `promtail`, `loki`, and `grafana`, we can monitor system and application logs in real time.

## Components of the Logging Stack

### **Grafana**

`grafana` is a visualization and monitoring tool used to analyze logs collected by `loki`.

- Acts as the front-end for querying and visualizing logs.
- Allows users to create dashboards for log monitoring.
- Queries logs from `loki` and displays them in an interactive UI.

### **Loki**

`loki` is a log aggregation system that stores logs and provides an efficient way to query them.

- Collects and indexes logs sent by `promtail`.
- Stores logs in a local file system.

#### How it works:

  - Receives logs from `promtail`.
  - Stores logs with metadata (labels) for quick retrieval.
  - Responds to `grafana` queries for log visualization.

### **Promtail**

`promtail` is a log shipper that forwards log files to `loki`.

- Collects logs from the Flask application and system logs, then sends them to `loki`.
- Tags logs with metadata (labels) for easier querying.

#### How it works:

  - Monitors the specified log directories.
  - Sends logs to `loki` for storage and retrieval.

## Running the Logging Stack

To start the logging stack, navigate to the monitoring folder and run:

```bash
sudo docker-compose up -d
```

## Accessing the Services

- **`grafana` UI:** `<http://localhost:3000>` (Default credentials: `admin/admin`)
- **`loki` API:** `<http://localhost:3100>`
- **`promtail` Logs:** 

Check logs using Docker logs:

  ```bash
  sudo docker-compose logs <loki/grafana/promtail/python_app>
  ```

## Adding `loki` as a Data Source in `grafana`

1. Open `grafana` and log in.

2. Navigate to **Settings > Data Sources**.

3. Click **Add data source** and select `loki`.

![Screenshot_28.jpg](Data%20for%20report/Screenshot_28.jpg)

4. Set the **URL** to `http://loki:3100` and click **Save & Test**.

5. Create queries and dashboards to visualize logs.

![Screenshot_29.jpg](Data%20for%20report/Screenshot_29.jpg)

(To the folder **Data for report** I have attached some logs that I saved while working in **PyCharm**)