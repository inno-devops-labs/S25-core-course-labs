# Logging via Grafan/Loki/Promtail Stack

## Grafana
Grafana is a tool that allows to display in a visual format logs and metrics for applications that are connected/related to Grafana.
In this case, I use Grafana docker-image with the Datasource setting which includes `Loki`.
This is done so that when you access `Grafana/Datasources` in the browser, Loki has already been created and connected.

## Loki
Loki is an easy log storage system. It stores app logs, indexes them by location and allows for fast search.
I used Loki too via docker-image with `volume and config` because Loki needs to keep intermediate logs somewhere.

## Promtail
Promtail collects logs from the sources listed and sends them to Loki. Applications do not use specific logfiles, so Promtail collects logs from all working Docker containers.
Also works with docker-image and a separate `config-file` because it needs a separate file to specify the resources from which the logs will be collected.

## Applications: Python App & NodeJS App
Application written in Python has port 8000 for default, and an application written in NodeJS has port 3000 for default.
Since port 3000 was already occupied under Grafana, I redefined it on the host to 8080. But Loki also allows you to get logs from this container.

## Container Logs:
* [NodeJS-log1](app-logs/nodejs-app-log1.png)
* [NodeJS-log2](app-logs/nodejs-app-log2.png)
* [NodeJS-log3](app-logs/nodejs-app-log3.png)
* [Python-log1](app-logs/python-app-log1.png)
* [Python-log2](app-logs/python-app-log2.png)
* [Python-log3](app-logs/python-app-log3.png)
* [Docker logs for successful running](app-logs/total-log.png)
